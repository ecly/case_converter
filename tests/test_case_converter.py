"""
Copyright (c) 2019 Emil Lynegaard
Distributed under the MIT software license, see the
accompanying LICENSE.md or https://opensource.org/licenses/MIT
"""

import unittest

from case_converter import convert


class TestCaseConverter(unittest.TestCase):
    def test_lower_camel_to_camel(self):
        self.assertEqual(convert("fooBarBaz", "camelCase", "CamelCase"), "FooBarBaz")
        self.assertEqual(convert("fooBar", "camelCase", "CamelCase"), "FooBar")
        self.assertEqual(convert("foo", "camelCase", "CamelCase"), "Foo")

    def test_snake_to_macro(self):
        self.assertEqual(
            convert("foo_bar_baz", "snake_case", "MACRO_CASE"), "FOO_BAR_BAZ"
        )
        self.assertEqual(convert("foo_bar", "snake_case", "MACRO_CASE"), "FOO_BAR")
        self.assertEqual(convert("foo", "snake_case", "MACRO_CASE"), "FOO")

    def test_macro_to_camel(self):
        self.assertEqual(convert("FOO_BAR_BAZ", "MACRO_CASE", "CamelCase"), "FooBarBaz")
        self.assertEqual(convert("FOO_BAR", "MACRO_CASE", "CamelCase"), "FooBar")
        self.assertEqual(convert("FOO", "MACRO_CASE", "CamelCase"), "Foo")

    def test_bad_cases_raises_assertion_error(self):
        with self.assertRaises(ValueError):
            convert("FooBar", "PASCAL_CASE", "unknown")
            convert("FooBar", "CamelCase", "unknown")
            convert("FooBar", "unknown", "snake_case")


if __name__ == "__main__":
    unittest.main()
