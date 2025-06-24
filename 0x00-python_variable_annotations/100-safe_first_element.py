#!/usr/bin/env python3
'''Duck typing - safe first element'''
from typing import Sequence, Any, Union, NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    '''
    safe_first_element - returns the first element of a sequence
    @lst: a sequence of any type
    Return: the first element of a sequence or None if the
    sequence is empty
    '''
    if lst:
        return lst[0]
    else:
        return None
