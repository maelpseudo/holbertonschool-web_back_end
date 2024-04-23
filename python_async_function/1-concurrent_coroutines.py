#!/usr/bin/env python3
# 1-concurrent_coroutines.py
import asyncio
from typing import List

# Assuming wait_random is defined in the module '0-basic_async_syntax'
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
    n (int): The number of times to spawn wait_random.
    max_delay (int): The maximum delay passed to wait_random.

    Returns:
    List[float]: A list of float delays from each wait_random call, returned in ascending order of completion.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed_delays = []

    for future in asyncio.as_completed(tasks):
        result = await future
        completed_delays.append(result)

    return completed_delays
