#!/usr/bin/env python3
# 3-tasks.py
import asyncio
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task that runs wait_random with the specified max_delay.

    Args:
    max_delay (int): The maximum delay that wait_random will use.

    Returns:
    asyncio.Task: A task that runs the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
