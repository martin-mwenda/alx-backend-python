#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine `wait_random` that
waits for a random delay between 0 and `max_delay` seconds.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay time in seconds.
    """
    delay: float = random.uniform(0, max_delay)  # Generate random delay
    await asyncio.sleep(delay)                   # Pause for the delay
    return delay
