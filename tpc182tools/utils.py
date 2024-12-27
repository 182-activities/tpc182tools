"""
Utility functions that are useful for processing the TPC 182 data.
"""

import numpy as np
from numpy.typing import NDArray

def pedsub(array: NDArray, axis: int=0) -> NDArray:
    """ Pedestal subtract the given array. """
    return array - np.median(array, axis=axis)
