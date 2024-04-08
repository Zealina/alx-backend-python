#!/usr/bin/env python3
"""Test utils.py module"""

from parameterized import parameterized  # type: ignore
from typing import Any, Mapping, Sequence, Dict
import unittest
from unittest.mock import patch, MagicMock
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test cases fkr the access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Any) -> None:
        """test the method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence) -> None:
        """Test access nested map exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """get_json test cases"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('requests.get')
    def test_get_json(
            self,
            url: str,
            test_payload: Dict,
            mock_request: MagicMock) -> None:
        """test the get_json logic"""
        mock_json = MagicMock()
        mock_json.json.return_value = test_payload
        mock_request.return_value = mock_json
        self.assertEqual(get_json(url), test_payload)
        mock_request.assert_called_once()
