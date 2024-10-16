#!/usr/bin/env python3
"""Async Generator"""

import asyncio
from typing import Any
from collections.abc import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, Any]:
    """Async Generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield i
