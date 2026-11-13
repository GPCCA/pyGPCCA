# Acknowledgments

We thank [Marcus Weber][] and the Computational Molecular Design ([CMD][]) group at the Zuse Institute Berlin ([ZIB][])
for the longstanding and productive collaboration in the field of Markov modeling of non-reversible molecular dynamics.
M. Weber, together with Susanna Röblitz and K. Fackeldey, had the original idea to employ Schur
vectors instead of eigenvectors in the coarse-graining of non-reversible transition matrices.
Further, we would like to thank [Fabian Paul][] for valuable discussions regarding the sorting of Schur vectors and his
effort to translate the original sorting routine for real Schur forms, SRSchur published by [Jan Brandts][],
from MATLAB into [Python code][],
M. Weber and [Alexander Sikorski][] for pointing us to [SLEPc][] for sorted partial Schur decompositions,
and A. Sikorski for supplying us with an [code example][] and guidance how to interface SLEPc in Python.
The development of _pyGPCCA_ started - based on the original [GPCCA][] program written in MATLAB - at the beginning of
2020 in a fork of [MSMTools][], since it was planned to integrate GPCCA into MSMTools at this time.
Due to this, some similarities in structure and code (indicated were evident) can be found.
Further, utility functions found in [pygpcca/utils/\_utils.py][utils] originate from MSMTools.

[marcus weber]: https://www.zib.de/members/weber
[cmd]: https://www.zib.de/numeric/cmd
[zib]: https://www.zib.de/
[fabian paul]: https://github.com/fabian-paul
[jan brandts]: https://www.math.uu.nl/publications/preprints/1180.pdf
[python code]: https://gist.github.com/fabian-paul/14679b43ed27aa25fdb8a2e8f021bad5
[alexander sikorski]: https://www.zib.de/members/sikorski
[slepc]: https://slepc.upv.es/
[code example]: https://github.com/zib-cmd/cmdtools/blob/1c6b6d8e1c35bb487fcf247c5c1c622b4b665b0a/src/cmdtools/analysis/pcca.py#L64
[gpcca]: https://github.com/msmdev/gpcca
[msmtools]: https://github.com/markovmodel/msmtools
[utils]: https://github.com/GPCCA/pyGPCCA/blob/main/src/pygpcca/utils/_utils.py
