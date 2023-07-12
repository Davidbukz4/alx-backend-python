#!/usr/bin/env python3
'''
Tasks
'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Returns a list of delays in float '''
    res = await asyncio.gather(*(task_wait_random(max_delay)
                               for i in range(n)))
    # sort the list in ascending order
    for i in range(len(res)):
        for j in range(i+1, len(res)):
            if (res[i] > res[j]):
                res[i], res[j] = res[j], res[i]

    return res
