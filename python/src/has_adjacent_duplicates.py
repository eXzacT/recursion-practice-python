from common import time_execution
import string


@time_execution()
def has_adjacent_duplicates_iter(s: str) -> bool:
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return True
    return False


@time_execution()
def has_adjacent_duplicates_rec(s: str) -> bool:
    def helper(idx: int) -> bool:
        if idx == len(s):
            return False
        if s[idx] == s[idx-1]:
            return True
        return helper(idx+1)

    return helper(1)


@time_execution(isTrampoline=True)
def has_adjacent_duplicates_gen(s: str) -> bool:
    def helper(idx: int) -> bool:
        if idx == len(s):
            yield False
        if s[idx] == s[idx-1]:
            yield True
        yield helper(idx+1)

    return helper(1)


print(has_adjacent_duplicates_iter(string.ascii_lowercase))
print(has_adjacent_duplicates_iter(string.ascii_lowercase+'z'))
print(has_adjacent_duplicates_rec(string.ascii_lowercase))
print(has_adjacent_duplicates_rec(string.ascii_lowercase+'z'))
print(has_adjacent_duplicates_gen(string.ascii_lowercase*1000))
print(has_adjacent_duplicates_gen(string.ascii_lowercase*1000+'z'))
