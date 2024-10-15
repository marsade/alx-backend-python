#!/usr/bin/python3
'''Async generator script'''
import asyncio


async def async_generator():
    '''Async generator function'''
    for i in range(10):
        asyncio.sleep(1)
        yield i
