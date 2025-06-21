#!/usr/bin/env python3
'''List of floats annotations'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    sum = 0
    for i in input_list:
        sum = sum + i
    return sum
