# pyGPCCA - Generalized Perron Cluster Cluster Analysis

[![PyPI][badge-pypi]][pypi]
[![Conda][badge-conda]][conda]
[![Cite][badge-cite]][reuter19]
[![Zenodo][badge-zenodo]][zenodo]
[![Tests][badge-tests]][tests]
[![Documentation][badge-docs]][documentation]
[![Coverage][badge-coverage]][coverage]
[![PyPI downloads][badge-downloads]][downloads]

[badge-pypi]: https://img.shields.io/pypi/v/pygpcca
[badge-conda]: https://img.shields.io/conda/vn/conda-forge/pygpcca
[badge-cite]: https://img.shields.io/badge/DOI-10.1063%2F1.5064530-blue
[badge-zenodo]: https://zenodo.org/badge/DOI/10.5281/zenodo.6914001.svg
[badge-tests]: https://img.shields.io/github/actions/workflow/status/GPCCA/pyGPCCA/test.yaml?branch=main
[badge-docs]: https://img.shields.io/readthedocs/pygpcca
[badge-coverage]: https://img.shields.io/codecov/c/github/GPCCA/pyGPCCA/main
[badge-downloads]: https://static.pepy.tech/personalized-badge/pygpcca?period=total&units=international_system&left_color=grey&right_color=blue&left_text=pypi%20downloads

Generalized Perron Cluster Cluster Analysis program to coarse-grain reversible and non-reversible Markov state models.

Markov state models (MSM) enable the identification and analysis of metastable states and related kinetics in a
very instructive manner. They are widely used, e.g., to model molecular or cellular kinetics.
Common state-of-the-art Markov state modeling methods and tools are very well suited to model reversible processes in
closed equilibrium systems. However, most are not well suited to deal with non-reversible or even non-autonomous
processes of non-equilibrium systems.
To overcome this limitation, the Generalized Robust Perron Cluster Cluster Analysis (GPCCA or G-PCCA) was developed.
The GPCCA method implemented in the _pyGPCCA_ program readily handles equilibrium as well as non-equilibrium data by
utilizing real Schur vectors instead of eigenvectors.
_pyGPCCA_ enables the semiautomatic coarse-graining of transition matrices representing the dynamics of the system
under study. Utilizing _pyGPCCA_, metastable states as well as cyclic kinetics can be identified and modeled.

<!-- end-intro -->

## Installation

_pyGPCCA_ requires Python 3.12 or newer. Install it from [conda-forge][conda], which also ships [PETSc][]/[SLEPc][]:

```bash
conda install -c conda-forge pygpcca
```

or from [PyPI][]:

```bash
pip install pygpcca
# or with PETSc/SLEPc
pip install "pygpcca[slepc]"
```

See the [installation guide][installation] for details and troubleshooting.

## Example

See the [example][] in the documentation.

## How to cite pyGPCCA

If you use _pyGPCCA_ to model molecular dynamics, e.g. to coarse-grain protein conformational dynamics, cite
[Reuter et al. (2018)][reuter18]. In a more general context, e.g. to model cellular dynamics, cite
[Reuter et al. (2019)][reuter19]. Please also cite the version of _pyGPCCA_ you used, as deposited on [Zenodo][].
BibTeX entries are in the [documentation][citation].

## Key contributors

- [Bernhard Reuter](https://github.com/msmdev): lead developer, maintainer
- [Michal Klein](https://github.com/michalk8): developer, diverse contributions
- [Marius Lange](https://github.com/Marius1311): developer, maintainer

[pypi]: https://pypi.org/project/pygpcca/
[conda]: https://anaconda.org/conda-forge/pygpcca
[zenodo]: https://doi.org/10.5281/zenodo.6913970
[reuter18]: https://doi.org/10.1021/acs.jctc.8b00079
[reuter19]: https://doi.org/10.1063/1.5064530
[tests]: https://github.com/GPCCA/pyGPCCA/actions/workflows/test.yaml
[documentation]: https://pygpcca.readthedocs.io/
[coverage]: https://codecov.io/gh/GPCCA/pyGPCCA
[downloads]: https://pepy.tech/project/pygpcca
[installation]: https://pygpcca.readthedocs.io/en/latest/installation.html
[example]: https://pygpcca.readthedocs.io/en/latest/example.html
[citation]: https://pygpcca.readthedocs.io/en/latest/how_to_cite.html
[petsc]: https://petsc.org/
[slepc]: https://slepc.upv.es/
