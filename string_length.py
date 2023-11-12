# Length of a string using recursion
from common import tramp, generate_string_repetition
import string


def string_length(s: str) -> int:
    counter = 0
    for _ in s:
        counter += 1
    return counter


def string_length_rec_tail(s: str, acc=0) -> int:
    if not s:
        return acc

    return string_length_rec_tail(s[1:], acc+1)


def string_length_rec_tail_idx(s: str) -> int:
    # No extra memory from copying the array but using try-except is a bit weird
    def helper(idx: int):
        try:
            s[idx]
        except:
            return idx

        return helper(idx+1)
    return helper(0)


def string_length_rec_tail_idx_gen(s: str) -> int:

    def helper(idx: int):
        try:
            s[idx]
        except:
            yield idx

        yield helper(idx+1)
    yield helper(0)


alphabet = string.ascii_lowercase
alphabet_repetition = generate_string_repetition(alphabet, 100_000)
print(string_length("pero"))
print(string_length_rec_tail("pero"))
print(string_length_rec_tail_idx("pero"))

# print(string_length_rec_tail(alphabet_repetition))
print(tramp(string_length_rec_tail_idx_gen, alphabet_repetition))
