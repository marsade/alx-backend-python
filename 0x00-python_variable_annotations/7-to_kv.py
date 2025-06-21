#!/usr/bin/env python3
'''Complex types annotations'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Return a tuple with the string representation of k
    and the square of v'''
    return (k, v ** 2)
