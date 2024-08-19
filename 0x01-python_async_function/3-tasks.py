#!/usr/bin/env python3
""" This module provides a function to create an asyncio Task """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ Create and return an asyncio Task for wait_random with the given max_delay """
    task = create_task(wait_random(max_delay))
    return task
