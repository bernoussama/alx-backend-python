#!/usr/bin/env python3
"""
    Measure the runtime of the wait_n coroutine
"""
import asyncio
import time


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: float) -> float:
    """
    Measure the runtime of the wait_n coroutine
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
