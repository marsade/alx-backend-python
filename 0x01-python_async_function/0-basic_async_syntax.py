#!/usr/bin/env python3
'''The basics of async'''


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Simulates a delay between 0 and max_delay seconds.

    Returns: float, representing the delay in seconds.'''
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
