#!/usr/bin/env python3
'''Mixed list annotations'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Return the sum of a mixed list of integers and floats.'''
    sum = 0
    for i in mxd_lst:
        sum = sum + i
    return sum
