#!/usr/bin/env python3

"""
This module contains a new wait_n(0) function that calls task_wait_random(3)
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Function that spawns task_wait_random function n times with
    specified max_delay.

    Parameters:
    - n (int): Number of times to spawn task_wait_random.
    - max_delay (int): Maximum delay for task_wait_random.

    Returns:
    - List[float]: List of delays in ascending order.
    """
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]

    # execute tasks concurrently
    results = await asyncio.gather(*tasks)

    return sorted(results)
