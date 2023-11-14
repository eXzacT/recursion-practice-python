# Print reverse of a string using iteration & recursion
from common import tramp
import string


def reverse_string(s: str) -> str:
    reversed_str = ""
    for i in range(len(s)-1, -1, -1):
        reversed_str += s[i]
    return reversed_str


def reverse_string_rec(s: str) -> str:
    if not s:
        return ""
    curr = s[0]
    return reverse_string_rec(s[1:]) + curr


def reverse_string_tail_rec(s: str, res="") -> str:
    if not s:
        return res
    return reverse_string_tail_rec(s[1:], s[0] + res)


def reverse_string_tail_rec_idx(s: str, idx=0, acc="") -> str:
    if idx >= len(s):
        return acc
    curr = s[idx]
    return reverse_string_tail_rec_idx(s, idx+1, curr+acc)


def reverse_string_tail_rec_idx_helper(s: str) -> str:
    def helper(idx: int, acc="") -> str:
        if idx >= len(s):
            return acc
        curr = s[idx]
        return helper(idx+1, curr + acc)
    return helper(0)


def reverse_string_gen(s: str) -> str:
    def helper(idx: int, acc="") -> str:
        if idx >= len(s):
            return acc
        curr = s[idx]
        yield helper(idx+1, curr + acc)
    return helper(0)


alphabet = string.ascii_lowercase
repeated_alphabet = alphabet * 10_000

print(reverse_string(alphabet))
print(reverse_string_rec(alphabet))
print(reverse_string_tail_rec(alphabet))
print(reverse_string_tail_rec_idx(alphabet))
print(reverse_string_tail_rec_idx_helper(alphabet))
# print(reverse_string_tail_rec_idx_helper(repeated_alphabet))
print(tramp(reverse_string_gen, repeated_alphabet))
