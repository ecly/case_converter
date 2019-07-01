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
import random

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


def _dank_decode(encoded):
    def dankify_word(w):
        return "".join([c.upper() if random.random() > 0.5 else c.lower() for c in w])

    return " ".join([dankify_word(w) for w in encoded])


def _ultra_leet_decode(encoded):
    # https://www.dcode.fr/leet-speak-1337
    leet_dict = {
        "A": ["4", "/\\", "@", "∂", "/-\\"],
        "B": ["8", "13", "|3", "ß"],
        "C": ["(", "¢", "<", "[", "©"],
        "D": ["[)", "|>", "|)", "|]"],
        "E": ["3", "€", "є", "[-"],
        "F": ["|=", "ƒ", "/="],
        "G": ["6", "(_+"],
        "H": ["#", "/-/", "[-]", "]-[", ")-(", "(-)", ":-:", "|~|", "|-|", "]~[", "}{"],
        "I": ["1", "!", "|", "][", "]", ":"],
        "J": ["_|", "_/", "¿"],
        "K": ["X", "|<", "|{", "ɮ"],
        "L": ["£", "1_", "ℓ", "|_", "[_"],
        "M": ["|V|", "|\\/|", "/\\/\\", "/V\\"],
        "N": ["|V", "|\\|", "/\\/", "[\\]", "/V"],
        "O": ["[]", "0", "()", "°"],
        "P": ["|*", "|o", "|º", "|°", "/*"],
        "Q": ["¶", "(_,)", "()_", "0_", "°|", "<|", "0."],
        "R": ["2", "|?", "/2", "®", "Я", "|2"],
        "S": ["5", "$", "§", "_/¯"],
        "T": ["7", "†", "¯|¯"],
        "U": ["(_)", "|_|", "L|", "µ"],
        "V": ["\\/", "|/"],
        "W": ["\\/\\/", "vv", "'//", "\\^/", "\\V/", "\\|/", "\\_|_/", "\\_:_/"],
        "X": ["><", "}{", "×", ")("],
        "Y": ["`/", "φ", "¥", "'/"],
        "Z": ["≥", "7_", ">_"],
    }

    def leetify_word(w):
        return "".join(random.choice(leet_dict.get(c.upper(), c)) for c in w)

    return " ".join([leetify_word(w) for w in encoded])


def _leet_decode(encoded):
    leet_dict = {
        "A": "4",
        "B": "8",
        "C": "(",
        "E": "3",
        "H": "#",
        "I": "1",
        "O": "0",
        "R": "2",
        "S": "5",
        "T": "7",
    }

    def leetify_word(w):
        return "".join(leet_dict.get(c.upper(), c) for c in w)

    return " ".join([leetify_word(w) for w in encoded])


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
    assert case_from in _CASE_REGEX_MAP, "case_from should be one of: %s" % ", ".join(
        _CASE_REGEX_MAP.keys()
    )
    assert case_to in _CASE_REGEX_MAP, "case_from should be one of: %s" % ", ".join(
        _CASE_REGEX_MAP.keys()
    )

    from_reg = _CASE_REGEX_MAP[case_from]
    return _decode(_encode(text, from_reg), case_to)
