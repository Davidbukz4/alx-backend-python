#!/usr/bin/env python3
'''
Parameterize a unit test
'''
from unittest.mock import patch
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    ''' Tests access_nested_map method '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        ''' returns the expected '''
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        ''' test exception '''
        with assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual('KeyError({})'.format(expected), repr(e.exception))
