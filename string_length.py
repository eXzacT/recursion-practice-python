# Length of a string using recursion
from common import tramp
import string


def string_length(input_str: str) -> int:
    counter = 0
    for c in input_str:
        counter += 1
    return counter


def string_length_rec_tail(input_str: str, length=0) -> int:
    if not input_str:
        return length

    return string_length_rec_tail(input_str[1:], length+1)


def string_length_rec_tail_gen(input_str: str, length=0) -> int:
    if not input_str:
        yield length

    yield string_length_rec_tail_gen(input_str[1:], length+1)


alphabet = string.ascii_lowercase
alphabet_repetition = ''.join([alphabet for _ in range(1000)])
print(string_length("pero"))
# print(string_length_rec_tail(alphabet_repetition))
print(tramp(string_length_rec_tail_gen, alphabet_repetition))
