#!/usr/bin/env python3
"""task module"""

import asyncio
wait_r = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """return asyncio task"""
    task = asyncio.create_task(wait_r(max_delay))
    return task
