#!/usr/bin/env python3
"""
This script defines a type-annotated function `sum_list` that takes a list of 
floats and returns the sum as a float.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats, returning the result as a float.
    
    Parameters:
    input_list (List[float]): A list containing elements that are all floats.
    
    Returns:
    float: The sum of the elements in `input_list`, returned as a float.
    """
    return sum(input_list)
