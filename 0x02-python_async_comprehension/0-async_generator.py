#!/usr/bin/python3
'''Async generator script'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Async generator function'''
    for i in range(10):
        asyncio.sleep(1)
        yield random.uniform(0, 10)
