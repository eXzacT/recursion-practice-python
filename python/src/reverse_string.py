# Print reverse of a string using iteration & recursion
from common import time_execution
import string


@time_execution()
def reverse_string(s: str) -> str:
    reversed_str = ""
    for i in range(len(s)-1, -1, -1):
        reversed_str += s[i]
    return reversed_str


@time_execution()
def reverse_string_rec(s: str) -> str:
    def helper(s: str) -> str:
        if not s:
            return ""
        curr = s[0]
        return helper(s[1:]) + curr
    return helper(s)


@time_execution()
def reverse_string_tail_rec(s: str) -> str:
    def helper(s: str, res=""):
        if not s:
            return res
        return helper(s[1:], s[0] + res)
    return helper(s)


@time_execution()
def reverse_string_tail_rec_v2(s: str) -> str:
    string_len = len(s)

    def helper(idx=0, acc="") -> str:
        if idx >= string_len:
            return acc
        curr = s[idx]
        return helper(idx+1, curr+acc)
    return helper()


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

print(reverse_string(alphabet))
print(reverse_string_rec(alphabet))
print(reverse_string_tail_rec(alphabet))
print(reverse_string_tail_rec_v2(alphabet))
# print(reverse_string_tail_rec_idx_helper(repeated_alphabet))
print(reverse_string_gen(repeated_alphabet))
