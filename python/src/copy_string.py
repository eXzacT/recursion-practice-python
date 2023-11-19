# Function to copy string (Iterative and Recursive)
import string
from common import tramp


def copy_string_iter(s: str) -> str:
    copy = ''
    for c in s:
        copy += c

    return copy


def copy_string_rec(s: str) -> str:
    length = len(s)

    def helper(idx: int) -> str:
        if idx >= length:
            return ''
        return s[idx]+helper(idx+1)
    return helper(0)


def copy_string_taiL_rec(s: str) -> str:
    length = len(s)

    def helper(idx: int, acc='') -> str:
        if idx >= length:
            return acc
        curr = s[idx]
        return helper(idx+1, acc+curr)
    return helper(0)


def copy_string_gen(s: str) -> str:
    length = len(s)

    def helper(idx: int, acc='') -> str:
        if idx >= length:
            yield acc
        curr = s[idx]
        yield helper(idx+1, acc+curr)
    yield helper(0)


my_string = 'mystring'
a = copy_string_iter(my_string)
b = copy_string_rec(my_string)
c = copy_string_taiL_rec(my_string)

print(a == b == c)

alphabet = string.ascii_lowercase
repeated_alphabet = alphabet*1000
# print(copy_string_rec(repeated_alphabet))
print(tramp(copy_string_gen, repeated_alphabet))
