#!/usr/bin/env python3
"measure run time module"
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return run time of parallel coroutines"""
    st_time = time.time()
    awaitables = [async_comprehension() for i in range(4)]
    await asyncio.gather(*awaitables)
    end_time = time.time()
    return end_time - st_time
