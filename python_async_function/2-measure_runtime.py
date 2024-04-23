#!/usr/bin/env python3
# 2-measure_runtime.py
import asyncio
import time
from typing import Callable

# Assuming wait_n is defined in the module '1-concurrent_coroutines'
from 1-concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time of the wait_n function.

    Args:
    n (int): The number of times to run wait_random.
    max_delay (int): The maximum delay value for wait_random.

    Returns:
    float: The average time taken per call of wait_random.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

