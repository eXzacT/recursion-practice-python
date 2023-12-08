# First uppercase letter in a string (Iterative and Recursive)
import string
from common import time_execution, tramp


@time_execution()
def find_first_uppercase_letter_ascii(s: str) -> tuple[int, str] | None:
    for idx, char in enumerate(s):
        if ord(char) in range(65, 91):
            return (idx, char)


@time_execution()
def find_first_uppercase_letter(s: str) -> tuple[int, str] | None:
    for idx, char in enumerate(s):
        if char in string.ascii_uppercase:
            return (idx, char)


@time_execution()
def find_first_uppercase_letter_tail_rec(s: str) -> tuple[int, str] | None:
    length = len(s)

    def helper(idx=0):
        if idx >= length:
            return None
        if s[idx] in string.ascii_uppercase:
            return (idx, s[idx])
        return helper(idx+1)

    return helper(0)


@time_execution(isTrampoline=True)
def find_first_uppercase_letter_gen(s: str) -> tuple[int, str] | None:
    length = len(s)

    def helper(idx=0):
        if idx >= length:
            yield None
        if s[idx] in string.ascii_uppercase:
            yield (idx, s[idx])
        yield helper(idx+1)

    return helper(0)


noUpper = "nouppercase"
upper = "somewhereUpper"
alphabet = 100_000*string.ascii_lowercase+"Z"

print(find_first_uppercase_letter(noUpper))
print(find_first_uppercase_letter(upper))
print(find_first_uppercase_letter_tail_rec(upper))
print(find_first_uppercase_letter_tail_rec(noUpper))
print(tramp(find_first_uppercase_letter_gen, alphabet))
