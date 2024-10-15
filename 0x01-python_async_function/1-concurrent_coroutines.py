#!/usr/bin/env python3
"""
This module contains asynchronous coroutine functions for handling
concurrent tasks.
"""
import asyncio
from typing import List

# Import the wait_random coroutine from the previous module
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes `wait_random` n times concurrently, with max delay of max_delay.

    Args:
        n (int): The number of times to spawn `wait_random`.
        max_delay (int): The maximum delay for each `wait_random` call.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    # Run n instances of wait_random concurrently and gather their results
    waiting_times = await asyncio.gather(
            *[wait_random(max_delay) for _ in range(n)])

    # Return the list of delays in ascending order
    return sorted(waiting_times)
