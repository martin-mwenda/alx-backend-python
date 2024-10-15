#!/usr/bin/env python3
"""
This module defines an asynchronous function that spawns
multiple tasks to wait for random delays.
"""
import asyncio
from typing import List  # Corrected the import statement
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times and gathers the wait times.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A sorted list of wait times from the spawned tasks.
    """
    wait_times = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(n)]
    )
    return sorted(wait_times)
