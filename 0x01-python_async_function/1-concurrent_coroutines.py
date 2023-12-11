#!/usr/bin/python3

"""
This module contain a function that import the wait_random function
and creates a funciton wait_n to spawm wait_random
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    Function that spawns wait_random function n times with specified max_delay.

    Parameters:
    - n (int): Number of times to spawn wait_random.
    - max_delay (int): Maximum delay for wait_random.

    Returns:
    - List[float]: List of delays in ascending order.
    """
    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]

    # execute tasks concurently
    results = await asyncio.gather(*tasks)

    for result in results:
        delays.append(result)

    return sorted(delays)
