#!/usr/bin/python3

"""
This module contains a type-annotated sum_mixed_list function
It takes a list of integers and floats and returns their sum as a float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of integers and floats in the input list as a float.
    """
    return float(sum(mxd_lst))
