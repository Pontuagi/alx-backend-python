#!/usr/bin/env python3

"""
This module contains the function element_length with annotated parameters
and return values
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements from input list 'lst'
    and their respective lengths.
    """
    return [(i, len(i)) for i in lst]
