#!/usr/bin/python3

"""
This module contains a type-annotated to_kv function
It takes a string k and an int or float v as arguments
It returns a tuple with the string k as the first element
and the square of v as the second element
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with string k as the first element and
    the square of int/float v as the second element (annotated as float).
    """
    return (k, float(v * v))
