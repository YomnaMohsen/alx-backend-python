#!/usr/bin/env python3
"async comprehension module"
import random
import asyncio
from typing import Iterator
async_gen = __import__('0-async_generator').async_generator


async def async_comprehension() -> Iterator[float]:
    result = [item async for item in async_gen()]
    return result
