import string
from common import time_execution


@time_execution()
def find_first_uppercase_letter_ascii(s: str) -> int:
    for idx, char in enumerate(s):
        if 65 <= ord(char) <= 90:
            return idx

    return -1


@time_execution()
def find_first_uppercase_letter(s: str) -> int:
    for idx, char in enumerate(s):
        if str.upper(char) == char:
            return idx

    return -1


@time_execution()
def find_first_uppercase_letter_tail_rec(s: str) -> int:
    def helper(idx: int = 0):
        if idx == len(s):
            return -1
        if str.upper(s[idx]) == s[idx]:
            return idx
        return helper(idx+1)

    return helper()


@time_execution(isTrampoline=True)
def find_first_uppercase_letter_gen(s: str) -> int:
    def helper(idx: int = 0):
        if idx == len(s):
            yield -1
        if str.upper(s[idx]) == s[idx]:
            yield idx
        yield helper(idx+1)

    return helper()


noUpper = "nouppercase"
upper = "somewhereUpper"
alphabet = 100_000*string.ascii_lowercase+"Z"

print(find_first_uppercase_letter(noUpper))
print(find_first_uppercase_letter(upper))
print(find_first_uppercase_letter_tail_rec(upper))
print(find_first_uppercase_letter_tail_rec(noUpper))
print(find_first_uppercase_letter_gen(alphabet))
