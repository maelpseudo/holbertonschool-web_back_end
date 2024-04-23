#!/usr/bin/env python3
# 4-tasks.py
import asyncio
from 3-tasks import task_wait_random  # Assuming task_wait_random is correctly defined in 3-tasks.py

async def task_wait_n(n: int, max_delay: int) -> list:
    """
    Spawns a given number of task_wait_random tasks concurrently and collects their results.

    Args:
    n (int): The number of times to spawn task_wait_random tasks.
    max_delay (int): The maximum delay that task_wait_random will use.

    Returns:
    list: A list of float delays from each task_wait_random call, returned in the order of task completions.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)
    results.sort()  # Assure the list is sorted; removing if order is guaranteed by external factors.
    return results
