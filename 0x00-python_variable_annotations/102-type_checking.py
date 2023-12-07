#!/usr/bin/python3

"""
This module validatea a code using mypy
"""

from typing import List, Tuple, Union


def zoom_array(lst: List[int], factor: int = 2) -> Tuple[int, ...]:
    """
    Zooms into the given list by repeating each element a specified
    number of times.
    Args:
    - lst (List[int]): The list of integers to zoom into.
    - factor (int, optional): The factor by which each element should be
    repeated. Defaults to 2.
    Returns:
    - Tuple[int, ...]: A tuple containing the elements of the list,
    each repeated by the given factor.
    """
    zoomed_in: Tuple[int, ...] = tuple([
        item for item in lst
        for i in range(factor)
    ])
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
