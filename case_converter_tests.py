# pylint: disable=missing-docstring

import unittest
from case_converter import (
    convert,
    CAMEL_CASE,
    PASCAL_CASE,
    LOWER_CAMEL_CASE,
    LOWER_PASCAL_CASE,
    MACRO_CASE,
    SNAKE_CASE,
)


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

    def test_module_global_regex(self):
        self.assertEqual(convert("FOO_BAR_BAZ", MACRO_CASE, PASCAL_CASE), "FooBarBaz")
        self.assertEqual(convert("foo_bar", SNAKE_CASE, LOWER_CAMEL_CASE), "fooBar")
        self.assertEqual(convert("Foo", CAMEL_CASE, LOWER_PASCAL_CASE), "foo")

    def test_bad_cases_raises_assertion_error(self):
        with self.assertRaises(AssertionError):
            convert("FooBar", "PASCAL_CASE", "unknown")
            convert("FooBar", CAMEL_CASE, "unknown")
            convert("FooBar", "unknown", SNAKE_CASE)


if __name__ == "__main__":
    unittest.main()
