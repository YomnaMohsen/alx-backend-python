#!/usr/bin/env python3
"""mult coroutines module"""

from typing import List
import asyncio
wait_r = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values).
    The list of the delays should be in ascending order without using s
    ort() because of concurrency."""
    sorted_tasks = []
    res = [wait_r(max_delay) for _ in range(n)]
    for t in asyncio.as_completed(res):
        result = await t
        sorted_tasks.append(result)
    return sorted_tasks
