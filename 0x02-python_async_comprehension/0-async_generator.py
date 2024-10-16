#!/usr/bin/env python3
"""
This module defines an asynchronous generator coroutine.

The coroutine, `async_generator`, loops 10 times, asynchronously waits for
1 second in each iteration, and then yields a random floating-point number
between 0 and 10.
"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers.

    This coroutine will:
    - Loop 10 times.
    - Asynchronously wait for 1 second in each iteration.
    - Yield a random float between 0 and 10 after each wait.

    Yields:
        float: A random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
