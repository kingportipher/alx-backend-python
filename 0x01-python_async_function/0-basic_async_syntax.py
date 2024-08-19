#!/usr/bin/env python3
"""
This module demonstrates the execution of an asynchronous coroutine in Python.
It imports the `wait_random` coroutine from another module and runs it with 
different `max_delay` values.
"""

import asyncio
from typing import Any


def main() -> None:
    """
    Execute the `wait_random` coroutine with various `max_delay` values 
    and print the results.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))


if __name__ == "__main__":
    main()
