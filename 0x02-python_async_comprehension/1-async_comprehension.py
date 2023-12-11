#!/usr/bin/env python3

"""
This function imports async_generator function from 0-async_generator.py
and uses in a coroutine called async_comprehensions
"""

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Coroutine collecting 10 random numbers using async comprehension
    over async_generator.

    Returns:
        list: List containing 10 random numbers generated asynchronously.
    """
    async_gen = async_generator()
    random_numbers = [number async for number in async_gen][:10]
    return random_numbers
