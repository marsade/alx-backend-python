#!/usr/bin/env python3
'''Mixed list annotations'''
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int | float]]) -> float:
    '''Return the sum of a mixed list of integers and floats.'''
    sum = 0
    for i in mxd_lst:
        sum = sum + i
    return sum
