#!/usr/bin/env python3
""" Import the first python file then writes async_comprehension.
    Which will collect 10 random numbers using an async comprehensing
    then return 10 random numbers. """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async comp """
    return [i async for i in async_generator()]
