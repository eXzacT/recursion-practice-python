# Print reverse of a string using iteration & recursion
from common import time_execution
import string


@time_execution()
def reverse_string_iter(s: str) -> str:
    reversed_str = ""
    for i in range(len(s)-1, -1, -1):
        reversed_str += s[i]

    return reversed_str


@time_execution()
def reverse_string_iter_double_pointers(s: str) -> str:
    l = 0
    r = len(s)-1
    chars = list(s)
    while l <= r:
        chars[l], chars[r] = chars[r], chars[l]
        l += 1
        r -= 1

    return ''.join(chars)


@time_execution()
def reverse_string_double_pointers_rec(s: str) -> str:
    def helper(chars: list[str], l: int, r: int) -> str:
        if l >= r:
            return ''.join(chars)
        chars[l], chars[r] = chars[r], chars[l]
        return helper(chars, l+1, r-1)

    return helper(list(s), 0, len(s)-1)


@time_execution()
def reverse_string_rec(s: str) -> str:
    def helper(s: str) -> str:
        if not s:
            return ""
        curr = s[0]
        return helper(s[1:]) + curr

    return helper(s)


@time_execution()
def reverse_string_backtrack(s: str) -> str:
    reversed_str = []

    def helper(idx: int) -> str:
        if idx == len(s):
            return
        helper(idx+1)
        reversed_str.append(s[idx])

    helper(0)
    return ''.join(reversed_str)


@time_execution()
def reverse_string_tail_rec(s: str) -> str:
    def helper(s: str, res=""):
        if not s:
            return res
        return helper(s[1:], s[0] + res)

    return helper(s)


@time_execution()
def reverse_string_tail_rec_v2(s: str) -> str:
    def helper(idx=0, acc="") -> str:
        if idx >= len(s):
            return acc
        return helper(idx+1, s[idx]+acc)

    return helper()


@time_execution()
def reverse_string_merge(s: str) -> str:
    def helper(s: str):
        if len(s) == 1:
            return s
        mid = len(s)//2
        return helper(s[mid:])+helper(s[:mid])

    return helper(s)


@time_execution(isTrampoline=True)
def reverse_string_gen(s: str) -> str:
    def helper(idx: int, acc="") -> str:
        if idx >= len(s):
            yield acc
        curr = s[idx]
        yield helper(idx+1, curr + acc)
    return helper(0)


alphabet = string.ascii_lowercase
repeated_alphabet = alphabet * 1000

print(reverse_string_iter(alphabet))
print(reverse_string_iter_double_pointers(alphabet))
print(reverse_string_double_pointers_rec(alphabet))
print(reverse_string_rec(alphabet))
print(reverse_string_backtrack(alphabet))
print(reverse_string_tail_rec_v2(alphabet))
print(reverse_string_tail_rec(alphabet))
print(reverse_string_merge(alphabet))
# print(reverse_string_tail_rec_idx_helper(repeated_alphabet))
print(reverse_string_gen(repeated_alphabet))
