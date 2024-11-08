#!/usr/bin/env python3
"""the utils module unit tests"""

import unittest
from parameterized import parameterized

from typing import (
    Dict,
    Mapping,
    Sequence,
    Union,
)
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Parameterize a unit test"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Union[Dict, int]
    ) -> None:
        """Tests access_nexted_map output"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence,
        exception: Exception,
    ) -> None:
        """Tests access_nested_map exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
