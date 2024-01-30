import pytest
from src.array_mean import *

test_cases = [
    ([num for num in range(1, 11)], 5.5),
    ([num for num in range(1, 100)], 50),
    ([0], 0),
]

functions = [globals()[name] for name in dir() if 'array_mean' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_ackermann(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(test_input) == expected
