"""
Utility functions that are useful for processing the TPC 182 data.
"""

__all__ = ["pedsub"]

import numpy as _np
from numpy.typing import NDArray as _NDArray


def pedsub(array: _NDArray, axis: int = 0) -> _NDArray:
    """ Pedestal subtract the given array. """
    return array - _np.median(array, axis=axis)
