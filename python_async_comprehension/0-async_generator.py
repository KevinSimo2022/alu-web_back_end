#!/usr/bin/env python3
""" a routine called async_generator which doesn't take any arguments and
    loops 10 times, each time asynchronously then waits before
     yielding a random number between 0 and 10. """
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """ async gen """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
