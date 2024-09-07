#!/usr/bin/env python3
"""
This script defines a function `element_length` that accepts an iterable of sequence-like objects 
and returns a list of tuples. Each tuple contains an element from the input iterable and its corresponding length.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each sequence in an iterable.
    
    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequence-like objects (e.g., strings, lists, tuples).
    
    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple consists of a sequence from the input 
    iterable and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
