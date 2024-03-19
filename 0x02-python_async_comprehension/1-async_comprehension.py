#!/usr/bin/env python3
"""Asynchronous comprehension module"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return Async generated floats in a list"""
    return [num async for num in async_generator()]
