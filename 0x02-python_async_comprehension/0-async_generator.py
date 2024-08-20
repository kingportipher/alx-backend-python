#!/usr/bin/env python3
"""
This module provides a function 
"""

from asyncio import Task, create_task
from 0_basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Create and return an asyncio Task for wait_random
    """
    return create_task(wait_random(max_delay))
