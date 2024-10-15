#!/usr/bin/env python3
'''Measures the execution time of an async generator function'''
import asyncio
import time
async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures the execution time of an async generator function

    Returns: float, representing the execution time in seconds'''
    start_time = time.time()
    run = await asyncio.gather(
        async_comp(),
        async_comp(),
        async_comp(),
        async_comp(),
    )
    end_time = time.time()
    return end_time - start_time
