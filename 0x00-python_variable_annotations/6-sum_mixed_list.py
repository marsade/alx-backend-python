#!/usr/bin/env python3
'''Mixed list annotations'''


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    sum = 0
    for i in mxd_lst:
        sum = sum + i
    return sum
