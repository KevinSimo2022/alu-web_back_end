#!/usr/bin/env python3
""" Import async_comprehension then write a
    measure_runtime routine which will execute async_comprehension 4x
    in parallel using asyncio.gather.
    measure_runtime will measure the total runtime and return it.
    """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure runtime """
    tasks = []
    start_time = time.time()
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
