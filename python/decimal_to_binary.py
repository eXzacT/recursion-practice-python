# Decimal to binary number using recursion and iteration
from common import tramp


def decimal_to_binary(num: int) -> str:
    res = ""
    while num / 2 > 0:
        remainder = num % 2
        num = num // 2
        res = str(remainder) + res
    return res


def decimal_to_binary_rec(num: int) -> str:
    if num == 0:
        return ""
    remainder = num % 2
    return decimal_to_binary_rec(num//2)+str(remainder)


def decimal_to_binary_tail_rec(num: int, binary_str="") -> str:
    if num == 0:
        return binary_str
    remainder = str(num % 2)
    return decimal_to_binary_tail_rec(num//2, remainder+binary_str)


def decimal_to_binary_gen(num: int, binary_str="") -> str:
    if num == 0:
        yield binary_str
    remainder = str(num % 2)
    yield decimal_to_binary_gen(num//2, remainder+binary_str)


print(decimal_to_binary(8))
print(decimal_to_binary_rec(8))
print(decimal_to_binary_tail_rec(8))
# print(decimal_to_binary_tail_rec(2**1000))
print(tramp(decimal_to_binary_gen, 2**1000))
