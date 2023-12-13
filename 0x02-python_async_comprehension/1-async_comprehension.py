#!/usr/bin/env python3

"""
This function imports async_generator function from 0-async_generator.py
and uses in a coroutine called async_comprehensions
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine collecting 10 random numbers using async comprehension
    over async_generator.

    Returns:
        list: List containing 10 random numbers generated asynchronously.
    """
    return [number async for number in async_generator()]
