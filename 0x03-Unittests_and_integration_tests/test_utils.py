#!/usr/bin/env/python3
'''Testing Utils.py'''

import unittest
from utils import access_nested_map
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    '''Test access_nested_map function'''
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a', ), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b')),
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        '''Test access_nested_map function with valid inputs'''
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()