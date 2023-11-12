# Function to copy string (Iterative and Recursive)
import string
from common import tramp, generate_string_repetition


def copy_string(s: str) -> str:
    copy = ''
    for c in s:
        copy += c

    return copy


def copy_string_rec(s: str) -> str:
    def helper(idx: int, acc='') -> str:
        if idx >= len(s):
            return acc
        curr = s[idx]
        return helper(idx+1, acc+curr)
    return helper(0)


def copy_string_rec_gen(s: str) -> str:
    def helper(idx: int, acc='') -> str:
        if idx >= len(s):
            yield acc
        curr = s[idx]
        yield helper(idx+1, acc+curr)
    yield helper(0)


x = 'mystring'
y = copy_string(x)
z = copy_string_rec(x)
print(y == z)

alphabet = string.ascii_lowercase
repeated_alphabet = generate_string_repetition(alphabet)
# print(copy_string_rec(repeated_alphabet))
print(tramp(copy_string_rec_gen, repeated_alphabet))
