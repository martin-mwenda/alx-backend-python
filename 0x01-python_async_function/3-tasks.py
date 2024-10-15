#!/usr/bin/env python3
"""
This module defines a function that creates an asyncio Task
for a coroutine with a specified maximum delay.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay to pass to wait_random.

    Returns:
        asyncio.Task: A task object that wraps the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
