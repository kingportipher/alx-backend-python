#!/usr/bin/env python3

"""
module provides a function to create an asyncio Task
"""
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[ float, None, None]:
    """
    Create and return an asyncio Task for wait_random with the given max_delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random( * 10
