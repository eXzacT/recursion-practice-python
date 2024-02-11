import pytest
from src.filename import *

test_cases = [
    ((1, 1), 3),
    ((0, 0), 1),
    ((3, 4), 125),
    ((0, 1), 2)
]

functions = [globals()[name] for name in dir() if 'filename' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_filename(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
