#!/usr/bin/env python3
"""measure run time module"""


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    st_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    ed_time = time.time()
    return (ed_time - st_time)/n
