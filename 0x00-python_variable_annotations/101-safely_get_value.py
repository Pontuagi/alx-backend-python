#!/usr/bin/python3

"""
This module contains a function with type annotations
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
            dct: Mapping,
            key: Any,
            default: Union[T, None] = None
            ) -> Union[Any, T]:
    """
    Returns the value associated with 'key' in 'dct' if it exists,
    otherwise returns 'default'.
    """
    if key in dct:
        return dct[key]
    else:
        return default
