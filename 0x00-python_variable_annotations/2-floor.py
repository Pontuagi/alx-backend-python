#!/usr/bin/python3

"""
This module contains a type-annotated floor function using
the math.floor function to get the floor of a float
"""


import math


def floor(n: float) -> int:
    """
    Returns the floor of the input float.
    """
    return math.floor(n)
