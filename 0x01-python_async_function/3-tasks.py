#!/usr/bin/env python3
'''Script to vreate an asyncio task'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates asyncio task

    Args: max_delay (int): Maximum delay in seconds
    Returns: asyncio.Task: An asyncio task'''
    return asyncio.create_task(wait_random(max_delay))
