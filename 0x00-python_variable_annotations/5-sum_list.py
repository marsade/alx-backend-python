#!/usr/bin/env python3
'''List of floats annotations'''


def sum_list(input_list: list[float]) -> float:
    sum = 0
    for i in input_list:
        sum = sum + i
    return sum
