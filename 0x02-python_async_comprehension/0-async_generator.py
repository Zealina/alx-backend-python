#!/usr/bin/env python3
"""Asynchronous generator module"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield random number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
