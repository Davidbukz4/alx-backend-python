#!/usr/bin/env python3
'''
Multiple Coroutines
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' Returns a list of delays in float '''
    res = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))

    for i in range(len(res)):
        for j in range(i+1, len(res)):
            if (res[i] > res[j]):
                res[i], res[j] = res[j], res[i]

    return res
