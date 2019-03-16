"""
Convert between programming naming conventions.
Supports:
    camelCase (pascalCase),
    CamelCase (PascalCase),
    snake_case,
    MACRO_CASE

Example usage:
    ```
    from case_converter import CAMEL_CASE, SNAKE_CASE

    case_converter.convert("MyValue", CAMEL_CASE, SNAKE_CASE")
    'my_value'

    case_converter.convert("fooBarBaz", "pascalCase", "MACRO_CASE")
    'FOO_BAR_BAZ'
    ```
"""
import re

CAMEL_CASE = "CamelCase"
PASCAL_CASE = CAMEL_CASE
LOWER_CAMEL_CASE = "camelCase"
LOWER_PASCAL_CASE = LOWER_CAMEL_CASE
SNAKE_CASE = "snake_case"
MACRO_CASE = "MACRO_CASE"

# Regex used for encoding various cases
_CAMEL_CASE_REGEX = re.compile("[A-Z][a-z]+")
_PASCAL_CASE_REGEX = _CAMEL_CASE_REGEX
_LOWER_CAMEL_CASE_REGEX = re.compile("[A-Z]?[a-z]+")
_LOWER_PASCAL_CASE_REGEX = _LOWER_CAMEL_CASE_REGEX
_SNAKE_CASE_REGEX = re.compile("[a-z]+")
_MACRO_CASE_REGEX = re.compile("[A-Z]+")

_CASE_REGEX_MAP = {
    "CamelCase": _CAMEL_CASE_REGEX,
    "PascalCase": _PASCAL_CASE_REGEX,
    "camelCase": _LOWER_CAMEL_CASE_REGEX,
    "pascalCase": _LOWER_PASCAL_CASE_REGEX,
    "snake_case": _SNAKE_CASE_REGEX,
    "MACRO_CASE": _MACRO_CASE_REGEX,
}


def _encode(text, case):
    return re.findall(case, text)


def _decode(encoded, case):
    if case == LOWER_CAMEL_CASE:
        return encoded[0].lower() + "".join([x.title() for x in encoded[1:]])

    if case == CAMEL_CASE:
        return "".join([x.title() for x in encoded])

    if case == SNAKE_CASE:
        return "_".join(encoded).lower()

    if case == MACRO_CASE:
        return "_".join(encoded).upper()

    raise ValueError("Unknown to case")


def convert(text, case_from, case_to):
    """
    Convert the `text` from `case_from` to `case_to`

    :param text:
        The text to have its case converted. Should already be in case `case_from`.
    :param case_from:
        The current case of the given `text`.
        Should be `str` representation of the case as found in `_CASE_REGEX_MAP`,
        Example: "snake_case"
    :param case_to:
        The case that the text should be converted to.
        Should be `str` representation of the case as found in `_CASE_REGEX_MAP`.
        Example: "CamelCase"
    """
    assert (
        case_from in _CASE_REGEX_MAP
    ), "case_from should be one of: %s" % ", ".join(_CASE_REGEX_MAP.keys())
    assert case_to in _CASE_REGEX_MAP, "case_from should be one of: %s" % ", ".join(
        _CASE_REGEX_MAP.keys()
    )

    from_reg = _CASE_REGEX_MAP[case_from]
    return _decode(_encode(text, from_reg), case_to)
