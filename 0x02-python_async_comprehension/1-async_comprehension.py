#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine `async_comprehension`.
"""

from . import async_generator  # Import async_generator from the previous file


async def async_comprehension():
  """
  This coroutine collects 10 random numbers.
  """
  return [await value async for value in async_generator()]
