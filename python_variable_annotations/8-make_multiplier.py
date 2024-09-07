#!/usr/bin/env python3
"""
This script defines a type-annotated function `make_multiplier` that returns 
a function capable of multiplying a given float by a specified multiplier.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a given float by the specified multiplier.
    
    Parameters:
    multiplier (float): The value by which the returned function will multiply its input.
    
    Returns:
    Callable[[float], float]: A function that takes a float as an argument and returns 
    a float, which is the result of multiplying the input by the multiplier.
    """
    def fn(n: float) -> float:
        """
        Multiplies the input by the multiplier.
        
        Parameters:
        n (float): The float value to be multiplied.
        
        Returns:
        float: The result of multiplying `n` by the outer multiplier.
        """
        return n * multiplier
    
    return fn
