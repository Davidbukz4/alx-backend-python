#!/usr/bin/env python3
'''
Complex types - functions
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' returns a multiplier function '''
    def fn(n: float) -> float:
        ''' multiplies a float by multiplier '''
        return n * multiplier

    return fn
