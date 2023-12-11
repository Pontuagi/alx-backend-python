#!/usr/bin/python3

"""
This module contains a function to measute the execution time of wait_n
function and the average time taken per iteration
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """
    Measure the average execution time for wait_n(n, max_delay).

    Parameters:
    - n (int): Number of times to call wait_n.
    - max_delay (int): Maximum delay for wait_n.

    Returns:
    - float: Average time taken per wait_n call.
    """
    start_time = time.time()

    # Measure execution time for wait_n)
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    return (total_time / n)
