#!/usr/bin/env python3

"""
This module contains a type-annotated make_multiplier function
It takes a float multiplier as an argument
Returns a function that can multiply a float by that multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
