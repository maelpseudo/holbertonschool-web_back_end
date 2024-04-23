#!/usr/bin/env python3
# 0-basic_async_syntax.py
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random time interval between 0 and max_delay seconds.

    Args:
    max_delay (int, optional): The maximum delay time in seconds. Defaults to 10.

    Returns:
    float: The actual delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
