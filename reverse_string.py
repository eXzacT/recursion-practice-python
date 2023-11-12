# Print reverse of a string using recursion
from common import tramp, generate_string_repetition
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


def reverse_string_rec_idx(s: str) -> str:
    def helper(start_idx):
        if start_idx < 0:
            return ""
        curr = s[start_idx]
        return curr+helper(start_idx-1)

    return helper(len(s)-1)


def reverse_string_rec_tail(s: str, res="") -> str:
    if not s:
        return res
    return reverse_string_rec_tail(s[1:], s[0] + res)


def reverse_string_rec_tail_idx(s: str, idx=0, acc="") -> str:
    if idx >= len(s):
        return acc
    curr = s[idx]
    return reverse_string_rec_tail_idx(s, idx+1, curr+acc)


def reverse_string_rec_tail_idx_helper(s: str) -> str:
    def helper(idx: int, acc="") -> str:
        if idx >= len(s):
            return acc
        curr = s[idx]
        return helper(idx+1, curr + acc)
    return helper(0)


def reverse_string_rec_tail_idx_gen(s: str, idx=0, acc="") -> str:
    if idx >= len(s):
        yield acc
    curr = s[idx]
    yield reverse_string_rec_tail_idx_gen(s, idx+1, curr+acc)


alphabet = string.ascii_lowercase
repeated_alphabet = generate_string_repetition(alphabet)

print(reverse_string("pero"))
print(reverse_string_rec("pero"))
print(reverse_string_rec_idx("pero"))
print(reverse_string_rec_tail_idx("pero"))
# print(reverse_string_rec_tail(alphabet_repetition))
# print(reverse_string_rec_tail_idx(alphabet_repetition))
print(tramp(reverse_string_rec_tail_idx_gen, repeated_alphabet))
