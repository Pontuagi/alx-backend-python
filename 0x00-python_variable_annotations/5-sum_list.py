#!/usr/bin/python3

"""
This module contains a type-annotated function sum_list
It takes a list input_list of floats as argument
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of floats in the input list.
    """
    return sum(input_list)
