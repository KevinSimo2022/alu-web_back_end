#!/usr/bin/env python3
""" make multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """type-annotated function make_multiplier taking a float multiplier
        as argument and returning a function that multiplies the float by
        the multiplier."""
    def fn(n: float):
        return n * multiplier
    return fn
