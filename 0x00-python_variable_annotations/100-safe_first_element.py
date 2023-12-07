#!/usr/bin/python3

"""
This module contains code that is augmented with duck-typed annotations
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Returns the first element of the sequence if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
