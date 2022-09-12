# Case Converter
Simple case converter for conversion between programming naming convention (and other fun cases).
Written in pure Python3 with zero dependencies.

## Usage
### Installation
`pip install .`

### Example
```sh
>>> from case_convert import convert; 
>>> convert('FooBarBaz', 'Camel', 'snake')
foo_bar_baz
>>>
>>> convert("I am very cool", "prose", "leet")
1 4m v32y (00l
>>> convert("WHAT_IS_YOUR_NAME", "MACRO_CASE", "dank")
"WhAt iS yOUr NAMe"
```

## Development
### Run tests
`python -m unittest`


## License
MIT License

Copyright (c) 2022 Emil Lynegaard

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
