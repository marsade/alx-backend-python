#!/usr/bin/env/python3
'''Testing Utils.py'''

import unittest
from typing import Mapping, Sequence
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    '''Test access_nested_map function'''
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a', ), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])

    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: int) -> None:
        '''Test access_nested_map function with valid inputs

        Args:
            nested_map (Mapping): A nested dictionary
            path (Sequence): A sequence of keys representing a path to the value
            expected (int): The expected value at the given path'''
        self.assertEqual(access_nested_map(nested_map, path), expected)
