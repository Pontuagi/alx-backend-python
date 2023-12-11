#!/usr/bin/env python3

"""
This module imports async_comprehension function and includes a
measure_runtime coroutine
"""

import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine to execute async_comprehension four times in parallel
    using asyncio.gather.

    Returns:
        float: Total runtime for executing async_comprehension four times
        in parallel.
    """
    start_time: float = asyncio.get_event_loop().time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time: float = asyncio.get_event_loop().time()
    return (end_time - start_time)
