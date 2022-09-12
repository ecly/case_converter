import unittest

from case_converter import convert
from case_converter.cases import CamelCase, LeetCase, LowerCamelCase, SnakeCase


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

    def test_decoder_only_as_encoder(self):
        with self.assertRaises(ValueError):
            self.assertEqual(
                convert("WhaT Is YouR NamE?", "dank", "snake_case"), "FooBarBaz"
            )

    def test_decoder_only_as_decoder(self):
        text = "Some regular text"

        dank = convert("Some regular text", "space", "dank")
        self.assertEqual(len(dank), len(text))

        leet = convert("Some regular text", "space", "leet")
        self.assertEqual(len(leet), len(text))

        ultra_leet = convert("Some regular text", "space", "ultraleet")
        self.assertGreaterEqual(len(ultra_leet), len(text))

    def test_bad_cases_raises_assertion_error(self):
        with self.assertRaises(ValueError):
            convert("FooBar", "PASCAL_CASE", "unknown")

        with self.assertRaises(ValueError):
            convert("FooBar", "CamelCase", "unknown")

        with self.assertRaises(ValueError):
            convert("FooBar", "unknown", "snake_case")

    def test_case_specified_as_type(self):
        self.assertEqual(convert("fooBarBaz", LowerCamelCase, CamelCase), "FooBarBaz")
        self.assertEqual(convert("fooBar", "camelCase", SnakeCase), "foo_bar")
        self.assertEqual(convert("foo", "camelCase", LeetCase), "f00")


if __name__ == "__main__":
    unittest.main()
