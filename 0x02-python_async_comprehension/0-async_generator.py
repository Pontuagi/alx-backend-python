#!/usr/bin/env python3

"""
This module contains an asynchronous generator function that yields random
numbers after an asynchronous delay.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
     Asynchronously generates random numbers after a delay.

    Yields:
        int: Random integers between 0 and 10.

    This generator asynchronously yields random floating-point numbers
    between 0 and 10, waiting for 1 second between each value.
    The generator loops 10 times before completion.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
