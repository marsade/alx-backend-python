#!/usr/bin/env python3
'''Testing Utils.py'''
import unittest
from unittest.mock import patch, PropertyMock
from typing import Mapping, Sequence, Type
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    '''Test access_nested_map function'''
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a', ), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        '''Test access_nested_map function with valid inputs

        Args:
            nested_map (Mapping): A nested dictionary
            path (Sequence): A sequence of keys representing
            a path to the value
            expected (int): The expected value at the given path'''
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)

    @parameterized.expand([
        ('empty_map', {}, ('a'), KeyError),
        ('wrong_path', {'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self, name, nested_map: Mapping,
                                         path: Sequence,
                                         expected_exception: Type[Exception]):
        '''Test access_nested_map function with invalid inputs

        Args:
            name (str): Test case name
            nested_map (Mapping): A nested dictionary
            path (Sequence): A sequence of keys representing
            a path to the value
            expected_exception (type): The expected exception type'''
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Test get_json function'''
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('https://holberton.io', {'payload': True}),
    ])
    def test_get_json(self, url: str, expected: Mapping):
        '''Test get_json function with valid inputs

        Args:
            url (str): A URL
            expected (Mapping): The expected JSON payload
        '''
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = expected
            res = get_json(url)

            mock_get.assert_called_once_with(url)
            self.assertEqual(res, expected)


class TestMemoize(unittest.TestCase):
    '''Test memoize decorator'''

    def test_memoize(self):
        '''Test the memoization decorator'''
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_object = TestClass()
            test_object.a_property()
            test_object.a_property()
            mock_method.assert_called_once()
