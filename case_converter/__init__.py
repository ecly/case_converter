"""
Copyright (c) 2022 Emil Lynegaard
Distributed under the MIT software license, see the
accompanying LICENSE.md or https://opensource.org/licenses/MIT

Convert between programming naming conventions.
Supported cases are:
    - camelCase (pascalCase)
    - CamelCase (PascalCase)
    - MACRO_CASE
    - snake_case
    - space case
    - dank (target only)
    - leet (target only)
    - ultraleet (target only)

The supported cases (including their aliases) can also be listed with:
    ```sh
    # encoders
    python -c "import case_converter; print(case_converter.ENCODERS.keys())"

    # decoders
    python -c "import case_converter; print(case_converter.DECODERS.keys())"
    ```


Example package usage:
    ```
    >>> from case_converter import convert
    >>> convert("MyVariable", "CamelCase", SNAKE_CASE")
    'my_variable'
    >>> convert("fooBarBaz", "pascalCase", "MACRO_CASE")
    'FOO_BAR_BAZ'
    >>> convert("WHAT_IS_YOUR_NAME", "MACRO_CASE", "dank")
    "WhAt iS yOUr NAMe"
    >>> convert("I am very cool", "space case", "leet")
    '1 4m v32y (00l'
    ```
"""
import importlib
import pkgutil

from case_converter.case_converter import convert
from case_converter.cases import (DECODERS, ENCODERS, CaseDecoder,
                                  CaseEncoderDecoder)
