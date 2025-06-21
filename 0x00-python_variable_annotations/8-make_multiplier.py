#!/usr/bin/env python3
'''Complex functions - functions'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Return a function that multiplies a float by multiplier'''
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
