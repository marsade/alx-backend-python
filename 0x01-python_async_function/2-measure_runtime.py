#!/usr/bin/env python3
'''Measure the time taken by the wait_n coroutine.'''
from typing import List
import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Function to measure the time taken to execute wait_n coroutine.

    Args: n (int): Number of random delays to wait for.
    max_delay (int): Maximum delay in seconds.

    Returns: float, representing the execution time of wait_n coroutine.'''
    st = time.time()
    _ = asyncio.run(wait_n(n, max_delay))
    et = time.time()
    elapsed = et - st
    return elapsed / n
