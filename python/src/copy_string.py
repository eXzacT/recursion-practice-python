import string
from common import time_execution


@time_execution()
def copy_string_iter(s: str) -> str:
    copy = ''
    for c in s:
        copy += c

    return copy


@time_execution()
def copy_string_rec(s: str) -> str:
    length = len(s)

    def helper(idx: int) -> str:
        if idx >= length:
            return ''
        return s[idx]+helper(idx+1)
    return helper(0)


@time_execution()
def copy_string_taiL_rec(s: str) -> str:
    length = len(s)

    def helper(idx: int, acc='') -> str:
        if idx == length:
            return acc
        curr = s[idx]
        return helper(idx+1, acc+curr)
    return helper(0)


@time_execution(isTrampoline=True)
def copy_string_gen(s: str) -> str:
    length = len(s)

    def helper(idx: int, acc='') -> str:
        if idx >= length:
            yield acc
        curr = s[idx]
        yield helper(idx+1, acc+curr)
    yield helper(0)


my_string = 'mystring'
print(copy_string_iter(my_string))
print(copy_string_rec(my_string))
print(copy_string_taiL_rec(my_string))

alphabet = string.ascii_lowercase
repeated_alphabet = alphabet*1000
# print(copy_string_rec(repeated_alphabet))
print(copy_string_gen(repeated_alphabet))
