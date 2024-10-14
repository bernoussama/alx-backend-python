#!/usr/bin/env python3
"""
Concurrent tasks
"""

import asyncio


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Wait for n seconds
    """
    delays = await asyncio.gather(*[task_wait_random(max_delay) for _ in range(n)])

    return sorted(delays)
