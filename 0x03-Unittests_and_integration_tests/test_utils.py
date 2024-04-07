#!/usr/bin/env python3
"""Test utils.py module"""

from parameterized import parameterized # type: ignore
from typing import Any, Mapping, Sequence
import unittest
access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases fkr the access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any) -> Any:
        """test the method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
