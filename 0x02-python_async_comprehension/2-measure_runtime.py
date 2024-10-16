#!/usr/bin/env python3
"""
Module: Measure Runtime

This module imports async_comprehension and defines a coroutine to measure
the runtime of executing async_comprehension in parallel.
"""

import asyncio
import time

# Import async_comprehension from the module
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime for executing four
    async_comprehension calls in parallel."""
    # List to hold the asynchronous tasks
    async_tasks = []
    start_time = time.time()  # Start the timer

    # Create and append four tasks to the list
    for _ in range(4):
        async_tasks.append(asyncio.create_task(async_comprehension()))

    await asyncio.gather(*async_tasks)  # Run the tasks concurrently
    end_time = time.time()  # End the timer

    return end_time - start_time  # Return the total runtime
