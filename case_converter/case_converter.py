from inspect import isclass
from typing import Type, Union

from case_converter.cases import (DECODERS, ENCODERS, CaseDecoder,
                                  CaseEncoderDecoder)

CaseDecoderTypeOrName = Union[str, Type[CaseDecoder]]
CaseEncoderDecoderTypeOrName = Union[str, Type[CaseEncoderDecoder]]


def _get_encoder(case: CaseEncoderDecoderTypeOrName) -> CaseEncoderDecoder:
    if isclass(case) and issubclass(case, CaseDecoder):
        if not issubclass(case, CaseEncoderDecoder):
            raise ValueError(f"{case} is only supported as a target case")

        return case

    if case not in ENCODERS:
        supported_encoders = list(ENCODERS.keys())
        raise ValueError(
            f"{case} is not one among supported encoder cases: {supported_encoders}"
        )

    return ENCODERS[case]


def _get_decoder(case: CaseDecoderTypeOrName) -> CaseDecoder:
    if isclass(case) and issubclass(case, CaseDecoder):
        return case

    if case not in DECODERS:
        supported_decoders = list(DECODERS.keys())
        raise ValueError(
            f"{case} is not one among supported decoder cases: {supported_decoders}"
        )

    return DECODERS[case]


def convert(
    text: str, case_from: CaseEncoderDecoderTypeOrName, case_to: CaseDecoderTypeOrName
) -> str:
    """
    Convert the `text` from `case_from` to `case_to`.

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
    encoder = _get_encoder(case_from)
    decoder = _get_decoder(case_to)

    encoded = encoder.encode(text)
    return decoder.decode(encoded)
