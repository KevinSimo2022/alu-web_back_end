#!/usr/bin/env python3
"""
This script defines a type-annotated function `sum_mixed_list` that takes a list of 
integers and floats and returns the sum as a float.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floats, returning the result as a float.
    
    Parameters:
    mxd_lst (List[Union[int, float]]): A list containing elements that are either 
    integers or floats.
    
    Returns:
    float: The sum of the elements in `mxd_lst`, returned as a float.
    """
    return float(sum(mxd_lst))
