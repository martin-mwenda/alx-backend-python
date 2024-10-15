#!/usr/bin/env python3
"""
This script measures the average runtime of the `wait_n` function.
"""
import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total runtime for executing `wait_n(n, max_delay)`
    and returns the average time per task.

    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay for each task.

    Returns:
        float: The average execution time per task.
    """
    start_time = time.time()  # Start timing
    asyncio.run(wait_n(n, max_delay))  # Run the async function
    end_time = time.time()  # End timing

    total_time = end_time - start_time  # Total execution time
    return total_time / n  # Average time per task
