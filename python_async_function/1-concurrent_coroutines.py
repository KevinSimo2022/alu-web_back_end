#!/usr/bin/env python3
""" Import wait_random from the 0 python file,
    write an async routine taking in 2 int arguments:
    max_delay and n. You will spawn wait_random n times with the specified
    max_delay. wait_n returns the list of all the delays (float values). """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ This script multiplies routines simultaneously using async  """
    delays: List[float] = []
    all_delays: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)
    return all_delays
