#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine `task_wait_n`
"""

from typing import List

from . import task_wait_random  # Import task_wait_random from the previous file


async def task_wait_n(n: int, max_delay: int) -> List[float]:
  """
  Spawns n concurrent `task_wait_random` instances
  """
  tasks = [task_wait_random(max_delay) for _ in range(n)]
  return [await task for task in asyncio.as_completed(tasks)]

# For testing purposes, only run this block if the script is executed directly
if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  n = 5
  max_delay = 6
  result = loop.run_until_complete(task_wait_n(n, max_delay))
