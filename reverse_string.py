# Print reverse of a string using recursion
from common import tramp
import string
import timeit


def reverse_string(input_str: str) -> str:
    reversed_str = ""
    for i in range(len(input_str)-1, -1, -1):
        reversed_str += input_str[i]
    return reversed_str


def reverse_string_rec(input_str: str) -> str:
    if not input_str:
        return ""
    curr = input_str[0]
    return reverse_string_rec(input_str[1:]) + curr


def reverse_string_rec_idx(input_str: str) -> str:
    def helper(start_idx):
        if start_idx == 0:
            return input_str[start_idx]
        curr = input_str[start_idx]
        return curr+helper(start_idx-1)

    return helper(len(input_str)-1)


def reverse_string_rec_tail(input_str: str, res="") -> str:
    if not input_str:
        return res
    return reverse_string_rec_tail(input_str[1:], input_str[0] + res)


def reverse_string_rec_tail_idx(input_str: str) -> str:
    def helper(idx, res="") -> str:
        if idx == 0:
            return res+input_str[idx]
        curr = input_str[idx]
        return helper(idx-1, res + curr)
    return helper(len(input_str)-1)


def reverse_string_rec_tail_idx_gen(input_str: str) -> str:
    def helper(idx, res="") -> str:
        if idx == 0:
            yield res+input_str[idx]
        curr = input_str[idx]
        yield helper(idx-1, res + curr)
    yield helper(len(input_str)-1)


def reverse_string_rec_tail_gen(input_str: str, res="") -> str:
    if not input_str:
        yield res
    res = input_str[0] + res
    yield reverse_string_rec_tail_gen(input_str[1:], res)


# alphabet = ''.join([chr(letter) for letter in range(97, 123)])
alphabet = string.ascii_lowercase
alphabet_repetition = ''.join([alphabet for _ in range(1000)])
print(reverse_string("pero"))
print(reverse_string_rec("pero"))
print(reverse_string_rec_idx("pero"))
print(reverse_string_rec_tail_idx("pero"))
# print(reverse_string_rec_tail(alphabet_repetition))
# print(reverse_string_rec_tail_idx(alphabet_repetition))
print(tramp(reverse_string_rec_tail_idx_gen, alphabet_repetition))
print(tramp(reverse_string_rec_tail_gen, alphabet_repetition))
