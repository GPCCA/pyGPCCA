# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog][],
and this project adheres to [Semantic Versioning][].

[keep a changelog]: https://keepachangelog.com/
[semantic versioning]: https://semver.org/

## [Unreleased]

### Fixed

- Detect a cut through a complex conjugate pair whichever eigenvalue of the pair comes first, and return conjugate
  pairs from `method="brandts"` with the positive imaginary part first. With numpy/scipy linked against Apple
  Accelerate, `brandts` could cut a pair silently and return a non-invariant subspace
  [#68](https://github.com/GPCCA/pyGPCCA/issues/68).

## [1.1.0] - 2026-11-13

### Fixed

- Use `Mat.createVecs`, since petsc4py 3.26 removed `Mat.getVecs` [#67](https://github.com/GPCCA/pyGPCCA/pull/67).

### Changed

- Require Python 3.12 or newer.
- Move to the [scverse cookiecutter](https://github.com/scverse/cookiecutter-scverse) layout: `src/` layout,
  hatchling packaging with VCS-based versions, ruff, Markdown docs.

## [1.0.4] - 2022-10-31

### Fixed

- Fix 'Operation done in wrong order' error when calling SLEPc [#42](https://github.com/GPCCA/pyGPCCA/pull/42).
- Minor pre-commit/linting fixes [#39](https://github.com/GPCCA/pyGPCCA/pull/39),
  [#40](https://github.com/GPCCA/pyGPCCA/pull/40), [#41](https://github.com/GPCCA/pyGPCCA/pull/41),
  [#44](https://github.com/GPCCA/pyGPCCA/pull/44), [#45](https://github.com/GPCCA/pyGPCCA/pull/45),
  [#46](https://github.com/GPCCA/pyGPCCA/pull/46).
- Fix intersphinx numpy/scipy [#37](https://github.com/GPCCA/pyGPCCA/pull/37).

### Changed

- Update and improve documentation and README [#47](https://github.com/GPCCA/pyGPCCA/pull/47).

## [1.0.3] - 2022-02-13

### Fixed

- Fix CI, unpin some requirements, pin docs, enable doc linting [#25](https://github.com/GPCCA/pyGPCCA/pull/25),
  [#26](https://github.com/GPCCA/pyGPCCA/pull/26).
- Patch release preparation [#35](https://github.com/GPCCA/pyGPCCA/pull/35).

### Changed

- Print deviations, if a test is failing since a threshold is exceeded [#29](https://github.com/GPCCA/pyGPCCA/pull/29).
- Adjust too tight thresholds in some tests [#30](https://github.com/GPCCA/pyGPCCA/pull/30),
  [#34](https://github.com/GPCCA/pyGPCCA/pull/34).

## [1.0.2] - 2021-03-26

### Fixed

- Fix not catching `ArpackError` when computing stationary distribution and mypy-related linting issues
  [#21](https://github.com/GPCCA/pyGPCCA/pull/21).

### Changed

- Use PETSc/SLEPc, if installed, to speed up the computation of the stationary distribution
  [#22](https://github.com/GPCCA/pyGPCCA/pull/22).

## [1.0.1] - 2021-02-01

### Changed

- Minor improvements/fixes in README and acknowledgments.

## [1.0.0] - 2021-01-29

Initial release.
