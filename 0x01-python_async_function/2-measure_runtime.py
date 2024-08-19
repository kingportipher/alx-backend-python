#!/usr/bin/env python3
"""
This module provides a function to measure the average runtime of executing
multiple instances of the wait_n coroutine.
"""

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)

    """
    start = time()
    run(wait_n(n, max_delay))
    end = time()

    return (end - start) / n

