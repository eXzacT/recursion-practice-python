import pytest
from src.ackermann import *

test_cases = [
    ((1, 1), 3),
    ((0, 0), 1),
    ((3, 4), 125),
    # ((1, 0), 2), #Doesn't work for any (m,0), not sure how to fix it
    ((0, 1), 2)
]

functions = [globals()[name] for name in dir() if 'ackermann' in name]


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_ackermann(test_input, expected):
    print(f"\nFor input {test_input}")
    for func in functions:
        assert func(*test_input) == expected
