# pylint: disable=missing-docstring
from setuptools import setup

long_description = """
Convert between programming naming conventions, and other less formal ones.

From cases supported:
    camelCase (pascalCase),
    CamelCase (PascalCase),
    snake_case,
    MACRO_CASE

To cases supported:
    camelCase (pascalCase),
    CamelCase (PascalCase),
    snake_case,
    MACRO_CASE
"""

setup(
    name="case_converter",
    version="1.0",
    description="Convert between naming conventions",
    long_description=long_description,
    license="MIT",
    packages=[],
    author="Emil Lynegaard",
    author_email="ecly@mailbox.org",
    keywords=[
        "case",
        "convert",
        "naming",
        "camelcase",
        "snakecase",
        "pascalcase",
        "macrocase",
    ],
    url="https://github.com/ecly/case_converter",
)
