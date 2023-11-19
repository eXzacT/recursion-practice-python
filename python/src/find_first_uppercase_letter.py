# First uppercase letter in a string (Iterative and Recursive)
import string


def find_first_uppercase_letter_ascii(s: str) -> tuple[int, chr] | None:
    for idx, char in enumerate(s):
        if ord(char) in range(65, 91):
            return (idx, char)


def find_first_uppercase_letter(s: str) -> tuple[int, chr] | None:
    for idx, char in enumerate(s):
        if char in string.ascii_uppercase:
            return (idx, char)


def find_first_uppercase_letter_tail_rec(s: str) -> tuple[int, chr] | None:
    length = len(s)

    def helper(idx=0):
        if idx >= length:
            return None
        if s[idx] in string.ascii_uppercase:
            return (idx, s[idx])
        return helper(idx+1)

    return helper(0)


noUpper = "nouppercase"
upper = "somewhereUpper"

print(find_first_uppercase_letter(noUpper))
print(find_first_uppercase_letter(upper))
print(find_first_uppercase_letter_tail_rec(upper))
print(find_first_uppercase_letter_tail_rec(noUpper))
