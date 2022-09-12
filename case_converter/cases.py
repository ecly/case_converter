import random
import re
from abc import ABC, abstractmethod
from inspect import isabstract
from typing import Dict, List

EncodedText = List[str]


class CaseDecoder(ABC):
    @property
    @abstractmethod
    def names(self) -> List[str]:
        ...

    @classmethod
    @abstractmethod
    def decode(cls, encoded: EncodedText) -> str:
        ...


class CaseEncoderDecoder(CaseDecoder):
    @classmethod
    def encode(cls, text: str) -> EncodedText:
        return re.findall(cls.regex, text)

    @property
    @abstractmethod
    def regex(self) -> re.Pattern:
        ...


class CamelCase(CaseEncoderDecoder):
    regex = re.compile("[A-Z][a-z]+")
    names = ["CamelCase", "PascalCase"]

    @classmethod
    def decode(cls, encoded):
        return "".join([x.title() for x in encoded])


class LowerCamelCase(CaseEncoderDecoder):
    regex = re.compile("[A-Z]?[a-z]+")
    names = ["camelCase", "pascalCase", "lowerCamelCase", "lowerPascalCase"]

    @classmethod
    def decode(cls, encoded):
        return encoded[0].lower() + "".join([x.title() for x in encoded[1:]])


class MacroCase(CaseEncoderDecoder):
    regex = re.compile("[A-Z]+")
    names = ["MACRO_CASE"]

    @classmethod
    def decode(cls, encoded):
        return "_".join(encoded).upper()


class SnakeCase(CaseEncoderDecoder):
    regex = re.compile("[a-z]+")
    names = ["snake_case"]

    @classmethod
    def decode(cls, encoded):
        return "_".join(encoded).lower()


class SpaceCase(CaseEncoderDecoder):
    regex = re.compile(r"\w+")
    names = ["space case", "prose"]

    @classmethod
    def decode(cls, encoded):
        return " ".join(encoded)


class DankCase(CaseDecoder):
    names = ["dank", "dank_case"]

    @staticmethod
    def _dankify_word(w):
        return "".join([c.upper() if random.random() > 0.5 else c.lower() for c in w])

    @classmethod
    def decode(cls, encoded):
        return " ".join([cls._dankify_word(w) for w in encoded])


class LeetCase(CaseDecoder):
    names = ["leet", "1337"]
    _leet_dict = {
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

    @classmethod
    def _leetify_word(cls, word: str) -> str:
        return "".join(cls._leet_dict.get(c.upper(), c) for c in word)

    @classmethod
    def decode(cls, encoded):
        return " ".join([cls._leetify_word(w) for w in encoded])


class UltraLeetCase(LeetCase):
    names = ["ultraleet", "ultra1337"]
    _leet_dict = {
        "A": ["4", "/\\", "@", "∂", "/-\\"],
        "B": ["8", "13", "|3", "ß"],
        "C": ["(", "¢", "<", "[", "©"],
        "D": ["[)", "|>", "|)", "|]"],
        "E": ["3", "€", "є", "[-"],
        "F": ["|=", "ƒ", "/="],
        "G": ["6", "(_+"],
        "H": [
            "#",
            "/-/",
            "[-]",
            "]-[",
            ")-(",
            "(-)",
            ":-:",
            "|~|",
            "|-|",
            "]~[",
            "}{",
        ],
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

    @classmethod
    def _leetify_word(cls, word):
        return "".join(random.choice(cls._leet_dict.get(c.upper(), c)) for c in word)


def __get_subclasses(cls):
    """https://stackoverflow.com/a/33607093"""
    for subclass in cls.__subclasses__():
        yield from __get_subclasses(subclass)
        yield subclass


ENCODERS: Dict[str, CaseEncoderDecoder] = {}
DECODERS: Dict[str, CaseEncoderDecoder] = {}
for cls_ in __get_subclasses(CaseDecoder):
    if isabstract(cls_):
        continue

    names = cls_.names
    supports_encoder = issubclass(cls_, CaseEncoderDecoder)
    for name in names:
        alt_name = re.sub("[ _]?(CASE|Case|case)", "", name)
        DECODERS[name] = cls_
        DECODERS[alt_name] = cls_
        if supports_encoder:
            ENCODERS[name] = cls_
            ENCODERS[alt_name] = cls_
