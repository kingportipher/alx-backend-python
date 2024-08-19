#!/usr/bin/env python3
"""
This module provides a function to create an asyncio Task 
for the wait_random coroutine.
"""

from asyncio import Task, create_task
from 0_basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Create and return an asyncio Task for wait_random with the given max_delay.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        Task: An asyncio Task object for the wait_random coroutine.
    """
    return create_task(wait_random(max_delay))

