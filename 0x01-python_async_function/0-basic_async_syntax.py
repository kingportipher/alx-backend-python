#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine `wait_random` that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: float = 10.0) -> float:
  """
  This coroutine waits for a random delay between 0 and the provided max_delay (inclusive) seconds.

  Args:
      max_delay (float, optional): The upper bound for the random delay (inclusive). Defaults to 10.0.

  Returns:
      float: The actual random delay that the coroutine waited for.
  """
  delay = random.uniform(0, max_delay)
  await asyncio.sleep(delay)
  return delay

# For testing purposes, only run this block if the script is executed directly
if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  tasks = [
      loop.run_in_executor(None, wait_random),
      loop.run_in_executor(None, wait_random, 5),
      loop.run_in_executor(None, wait_random, 15),
  ]
  results = loop.run_until_complete(asyncio.gather(*tasks))
  for result in results:
    print(result)
