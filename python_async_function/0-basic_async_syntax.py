#!/usr/bin/env python3
""" basic async syntax """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ asynch routine taking in an integer argument
         awaiting
        for a random delay between 0 and max_delay (included and float value)
        seconds and then returns it. """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
