#!/usr/bin/env python3
""" string and int or float to tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """type-annotated function to_kv that takes a string k and an int or float
        v as arguments and returns a tuple. The first element of the tuple is
        the string k. The 2nd element is the square of the int or float v and
        has to be annotated as a float."""
    return (k, v * v)
