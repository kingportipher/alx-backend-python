#!/usr/bin/env python3

"""
This module defines an asynchronous coroutine `measure_runtime`
"""

from . import async_comprehension  # Import async_comprehension from the previous file
import time


async def measure_runtime():
    """
    Measures the total runtime of executing `async_comprehension`
    """
    start_time = time.perf_counter()  # Get start time with high precision
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.perf_counter()
    return end_time - start_time
