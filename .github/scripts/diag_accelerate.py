"""Throwaway diagnostic for #68: where does `brandts` lose invariance when LAPACK comes from Apple Accelerate?

Prints, for the test matrix P_2 and random stochastic matrices:
- the BLAS/LAPACK backends;
- properties of the unsorted `scipy.linalg.schur` output (residual, orthogonality, 2x2 block standardisation,
  sub-diagonal entries that are tiny but nonzero);
- the residual after each Brandts swap, to locate the first bad swap;
- the same metrics for a LAPACK `dtrexc` sort.
"""

import sys
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import lapack, rsf2csf, schur, subspace_angles

import pygpcca._sort_real_schur as srs

np.set_printoptions(precision=3, linewidth=150)
EPS = np.finfo(float).eps


def load_P_2():
    src = (Path(__file__).parents[2] / "tests" / "conftest.py").read_text()
    i = src.index("def P_2():")
    j = src.index("@pytest.fixture", i)
    ns = {"np": np}
    exec(src[i:j], ns)  # noqa: S102
    return ns["P_2"]()


def blocks(R):
    n, i, out = R.shape[0], 0, []
    while i < n:
        s = 2 if i + 1 < n and R[i + 1, i] != 0 else 1
        out.append((i, s))
        i += s
    return out


def describe_schur(P, R, Q, label):
    n = P.shape[0]
    res = np.linalg.norm(P @ Q - Q @ R) / np.linalg.norm(P)
    orth = np.linalg.norm(Q.T @ Q - np.eye(n))
    low = np.abs(np.tril(R, -2)).max() if n > 2 else 0.0
    sub = np.diag(R, -1)
    tiny = [(i, f"{x:.1e}") for i, x in enumerate(sub) if 0 < abs(x) <= 100 * EPS]
    nonstd = []
    for i, s in blocks(R):
        if s == 2:
            a, b, c, d = R[i, i], R[i, i + 1], R[i + 1, i], R[i + 1, i + 1]
            if not (abs(a - d) <= 100 * EPS * max(1, abs(a)) and b * c < 0):
                nonstd.append((i, a, b, c, d))
    ev = np.diag(rsf2csf(R, Q)[0])
    first_imag = [int(np.sign(ev[i].imag)) for i, s in blocks(R) if s == 2]
    print(
        f"  [{label}] resid={res:.1e} orth={orth:.1e} max|tril(R,-2)|={low:.1e} "
        f"tiny-subdiag={tiny} non-standard 2x2={nonstd} sign(Im) of first eigenvalue per 2x2 block={first_imag}"
    )
    return ev


def top_invariance(P, Q, R, k):
    """Largest subspace angle between P Q[:, :j] and Q[:, :j] over block boundaries j <= k."""
    worst = []
    for j in range(1, k + 1):
        if j == P.shape[0] or R[j, j - 1] == 0:
            worst.append(subspace_angles(P @ Q[:, :j], Q[:, :j]).max())
    return max(worst)


def brandts_traced(P, k, z):
    R0, Q0 = schur(P, output="real")
    orig_swap = srs.swap
    log = []

    def traced_swap(U, S, v, w, inplace=False):
        U, S = orig_swap(U, S, v, w, inplace=inplace)
        log.append((v, w, np.linalg.norm(P @ U - U @ S) / np.linalg.norm(P)))
        return U, S

    srs.swap = traced_swap
    try:
        Q, R, ap = srs.sort_real_schur(Q0.copy(), R0.copy(), z=z, b=k)
    finally:
        srs.swap = orig_swap
    first_bad = next(((i, v, w, r) for i, (v, w, r) in enumerate(log) if r > 1e-10), None)
    return Q, R, ap, log, first_bad


def trexc_sort(P, k, z):
    R, Q = schur(P, output="real")
    pos, n = 0, P.shape[0]
    while pos < min(k, n):
        cand = [(i, s) for i, s in blocks(R) if i >= pos]

        def key(b):
            lam = np.linalg.eigvals(R[b[0] : b[0] + b[1], b[0] : b[0] + b[1]])[0]
            return abs(lam) if z == "LM" else lam.real

        i, _ = max(cand, key=key)
        R, Q, info = lapack.dtrexc(R, Q, i + 1, pos + 1)
        if info != 0:
            print(f"    dtrexc info={info}")
        pos += 2 if pos + 1 < n and R[pos + 1, pos] != 0 else 1
    return Q, R


def run(P, name):
    print(f"\n=== {name} (n={P.shape[0]})")
    R0, Q0 = schur(P, output="real")
    describe_schur(P, R0, Q0, "schur, unsorted")
    for z in ("LM", "LR"):
        for k in sorted({4, 6, P.shape[0] if P.shape[0] <= 12 else 15}):
            print(f" z={z} k={k}")
            Q, R, ap, log, first_bad = brandts_traced(P, k, z)
            ev = describe_schur(P, R, Q, "brandts")
            print(
                f"    brandts: swaps={len(log)} max ap={max(ap) if ap else 0:.1e} "
                f"top-k invariance angle={top_invariance(P, Q, R, k):.1e} first swap with resid>1e-10: {first_bad}"
            )
            print(f"    brandts eigenvalues[:k]={ev[:k]}")
            Q, R = trexc_sort(P, k, z)
            ev = describe_schur(P, R, Q, "dtrexc")
            print(f"    dtrexc: top-k invariance angle={top_invariance(P, Q, R, k):.1e}")
            print(f"    dtrexc eigenvalues[:k]={ev[:k]}")


if __name__ == "__main__":
    print(sys.version)
    print("numpy", np.__version__, "scipy", scipy.__version__)
    np.show_config()
    scipy.show_config()
    run(load_P_2(), "P_2")
    rng = np.random.default_rng(0)
    for n in (50, 200):
        A = rng.random((n, n)) ** 4
        run(A / A.sum(1, keepdims=True), f"random {n}")
