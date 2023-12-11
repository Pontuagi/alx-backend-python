#!/usr/bin/python3

"""
This module contains a function that define an asynchronous coroutine.
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    Function to generate a random float delay between 0 and max_delay
    and wait for the generated delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
