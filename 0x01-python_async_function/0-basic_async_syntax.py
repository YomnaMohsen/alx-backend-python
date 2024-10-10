#!/usr/bin/env python3
"""basics module"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits fro random time"""
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
