#!/usr/bin/env python3
'''Multiple coroutines with asyncio'''
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Function to wait for and collect n random delays.

        Args: n (int): Number of random delays to wait for.
            max_delay (int): Maximum delay in seconds.

        Returns: list of floats, representing the collected random delays.'''
    delay = []
    for _ in range(n):
        delay.append(await wait_random(max_delay))
    n = len(delay)

    for i in range(n):
        for j in range(0, n-i-1):
            if delay[j] > delay[j+1]:
                delay[j], delay[j+1] = delay[j+1], delay[j]

    return delay
