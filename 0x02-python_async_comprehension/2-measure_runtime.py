#!/usr/bin/env python3
'''Measures the execution time of an async generator function'''
import asyncio
import time
async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures the execution time of an async generator function

    Returns: float, representing the execution time in seconds'''
    start_time = time.perf_counter()
    task = [async_comp() for i in range(4)]
    await asyncio.gather(*task)
    end_time = time.perf_counter()
    return end_time - start_time
