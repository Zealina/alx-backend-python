#!/usr/bin/env python3
"""Measure runtime"""

import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure asynchronous run timr"""
    task = []
    for i in range(4):
        task.append(async_comprehension())
    start = time()
    result = await asyncio.gather(*task)
    end = time()
    return end - start
