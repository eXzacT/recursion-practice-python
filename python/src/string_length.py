# Length of a string using recursion
from common import tramp
import string


def string_len(s: str) -> int:
    counter = 0
    for _ in s:
        counter += 1
    return counter


def string_len_tail_rec(s: str, acc=0) -> int:
    if not s:
        return acc

    return string_len_tail_rec(s[1:], acc+1)


def string_len_tail_rec_helper(s: str) -> int:
    # No extra memory from copying the array but using try-except is a bit weird
    def helper(idx: int):
        try:
            s[idx]
        except:
            return idx

        return helper(idx+1)
    return helper(0)


def string_len_gen(s: str) -> int:
    def helper(idx: int):
        try:
            s[idx]
        except:
            yield idx  # We reached the end
        yield helper(idx+1)

    yield helper(0)


alphabet = string.ascii_lowercase
alphabet_repetition = alphabet*100_000
print(string_len("pero"))
print(string_len_tail_rec("pero"))
print(string_len_tail_rec_helper("pero"))
# print(string_len_tail_rec_helper(alphabet_repetition))
print(tramp(string_len_gen, alphabet_repetition))
