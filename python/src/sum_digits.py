from common import tramp
import functools
import itertools
# Sum digits of a given number


def sum_digits(num: int) -> int:
    num_str = str(num)
    digit_sum = 0
    for c in num_str:
        digit_sum += int(c)

    return digit_sum


def sum_digits_v2(num: int) -> int:
    digit_sum = 0
    while num > 0:
        digit = num % 10
        digit_sum += digit
        num //= 10
    return digit_sum


def sum_digits_rec(num: int) -> int:
    if num == 0:
        return 0
    digit = num % 10
    num //= 10
    return digit+sum_digits_rec(num)


def sum_digits_tail_rec(num: int) -> int:
    def helper(num: int, acc=0) -> int:
        if num == 0:
            return acc
        digit = num % 10
        num //= 10
        return helper(num, acc+digit)
    return helper(num)


def sum_digits_gen(num: int) -> int:
    def helper(num: int, acc=0) -> int:
        if num == 0:
            yield acc
        digit = num % 10
        num //= 10
        yield helper(num, acc+digit)
    return helper(num)


print(sum_digits(1234))
print(sum_digits_v2(1234))
print(sum_digits_rec(1234))
print(sum_digits_tail_rec(1234))
num_str = '5'*1000
num = int(num_str)
print(tramp(sum_digits_gen, num))

# Flexing
num_infinite_repetition = itertools.count(5, 0)  # override step to 0
num_arr = list(itertools.islice(num_infinite_repetition, 1000))
num = int(''.join(map(str, num_arr)))
print(tramp(sum_digits_gen, num))

# BONUS
print(functools.reduce(lambda a, b: int(a)+int(b), num_str))
# This one is for all the steps, but we can get the last one
print(list(itertools.accumulate(num_str, lambda a, b: int(a)+int(b)))[-1])
