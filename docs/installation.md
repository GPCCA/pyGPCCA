# Installation

_pyGPCCA_ requires Python 3.12 or newer. If any problems arise, please consult the [troubleshooting](#troubleshooting)
section.

## Conda

_pyGPCCA_ is available as a [conda package](https://anaconda.org/conda-forge/pygpcca) and can be installed as:

```bash
conda install -c conda-forge pygpcca
```

This is the recommended way of installing, since this package also includes [PETSc][]/[SLEPc][] libraries.
We use [PETSc][]/[SLEPc][] internally to speed up the computation of the leading Schur vectors. These are optional
dependencies - if they're not present, we compute a full Schur decomposition instead and sort it using the method
introduced by [Brandts (2001)][brandts]. Note that this scales cubically in sample number, making it essential to use
[PETSc][]/[SLEPc][] for large sample numbers. [PETSc][]/[SLEPc][] implement iterative methods to only compute
the leading Schur vectors, which is computationally much less expensive.

## PyPI

In order to install _pyGPCCA_ from [The Python Package Index](https://pypi.org/project/pygpcca/), run:

```bash
pip install pygpcca
# or with libraries utilizing PETSc/SLEPc
pip install "pygpcca[slepc]"
```

## Development version

If you want to use the development version of _pyGPCCA_ from [GitHub](https://github.com/GPCCA/pyGPCCA), run:

```bash
pip install git+https://github.com/GPCCA/pyGPCCA
```

## Troubleshooting

During the installation of `petsc`, `petsc4py`, `slepc`, and `slepc4py`, the following error(s) might appear:

```
ERROR: Failed building wheel for <package name>
```

However, this should be fine if in the end, it also outputs:

```
Successfully installed <package name>
```

To quickly verify that the packages have been installed, you can run:

```bash
python3 -c "import petsc4py; import slepc4py; print(petsc4py.__version__, slepc4py.__version__)"
```

### Debian-based systems

Below are alternative steps for installing [PETSc][]/[SLEPc][], in case any problems arise, especially when installing
from [PyPI](https://pypi.org/project/pygpcca/):

```bash
# install dependencies
sudo apt-get update -y
sudo apt-get install gcc gfortran libopenmpi-dev libblas-dev liblapack-dev petsc-dev slepc-dev -y

# install a message passing interface for Python
pip install --user mpi4py

# install petsc and petsc4py
pip install --user petsc
pip install --user petsc4py

# install slepc and slepc4py
pip install --user slepc
pip install --user slepc4py
```

### macOS

The most robust way is to follow the [PETSc installation guide][petsc-install] and the
[SLEPc installation guide][slepc-install].

The installation steps can be roughly outlined as:

```bash
# install dependencies
brew install gcc open-mpi openblas lapack arpack

# follow the PETSc installation steps
# follow the SLEPc installation steps

# install petsc4py
pip install --user petsc4py
# install slepc4py
pip install --user slepc4py
```

[brandts]: https://www.math.uu.nl/publications/preprints/1180.pdf
[petsc]: https://petsc.org/
[slepc]: https://slepc.upv.es/
[petsc-install]: https://petsc.org/release/install/
[slepc-install]: https://slepc.upv.es/documentation/instal.htm
