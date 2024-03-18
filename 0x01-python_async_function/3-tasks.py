#!/usr/bin/env python3
"""Create some function"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create a task object and return the object"""
    return asyncio.create_task(wait_random(max_delay))