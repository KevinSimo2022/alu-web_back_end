#!/usr/bin/env python3
"""
This script defines a type-annotated function `to_kv` that takes a string 
and an integer or float as arguments and returns a tuple. The tuple consists 
of the string and the square of the numeric value.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with a string and the square of a numeric value.
    
    Parameters:
    k (str): The string to be included as the first element of the tuple.
    v (Union[int, float]): A numeric value (either an integer or float) whose square 
    will be the second element of the tuple.
    
    Returns:
    Tuple[str, float]: A tuple where the first element is the string `k`, and the 
    second element is the square of `v`, annotated as a float.
    """
    return (k, float(v * v))
