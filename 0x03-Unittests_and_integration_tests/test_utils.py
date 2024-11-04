#!/usr/bin/env python3
"""test module"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap Module"""

    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, value):
        """test function access_nested_map"""
        self.assertEqual(access_nested_map(map, path), value)

    @parameterized.expand([
        ({}, "a", KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, map, path, error):
        with self.assertRaises(error):
            access_nested_map(map, path)

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
            ])
    @patch('requests.get')
    def test_get_json(self, url, payload, mock_get_request):
        """test get_json"""
  
        mock_jvalue = Mock(return_value=payload)
        mock_get_request.return_value.json = mock_jvalue
        result = get_json(url)
        self.assertEqual(result, payload)
        mock_get_request.assert_called_once_with(url)

class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        """test memoize method"""
        class TestClass:
            """test class"""
            def a_method(self):
                return 42
            @memoize
            def a_property(self):
                return self.a_method()