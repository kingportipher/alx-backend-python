#!/usr/bin/env python3
"""
This module demonstrates asynchronous programming in Python.
It imports and runs an asynchronous function that waits for a random delay.
"""

import asyncio
from typing import Any


def main() -> None:
    """Execute the wait_random coroutine with different max_delay values."""
    wait_random = __import__('0-basic_async_syntax').wait_random
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))


if __name__ == "__main__":
    main()
