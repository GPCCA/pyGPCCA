from importlib.metadata import version

from pygpcca._gpcca import GPCCA, gpcca_coarsegrain
from pygpcca.utils import stationary_distribution  # type: ignore[attr-defined]

__all__ = ["GPCCA", "gpcca_coarsegrain", "stationary_distribution"]

__version__ = version("pygpcca")
