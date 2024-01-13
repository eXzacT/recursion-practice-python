# Decimal to binary number using recursion and iteration
from common import time_execution


@time_execution()
def decimal_to_binary(num: int) -> str:
    res = ""
    while num > 0:
        remainder = num % 2
        num = num // 2
        res = str(remainder) + res
    return res


@time_execution()
def decimal_to_binary_rec(num: int) -> str:
    def helper(num: int) -> str:
        if num == 0:
            return ""
        return helper(num//2)+str(num % 2)
    return helper(num)


@time_execution()
def decimal_to_binary_tail_rec(num: int) -> str:
    def helper(num: int, binary_str="") -> str:
        if num == 0:
            return binary_str
        remainder = str(num % 2)
        return helper(num//2, remainder+binary_str)
    return helper(num)


@time_execution(isTrampoline=True)
def decimal_to_binary_gen(num: int) -> str:
    def helper(num: int, binary_str=""):
        if num == 0:
            yield binary_str
        remainder = str(num % 2)
        yield helper(num//2, remainder+binary_str)
    return helper(num)


print(decimal_to_binary(8))
print(decimal_to_binary_rec(8))
print(decimal_to_binary_tail_rec(8))
# print(decimal_to_binary_tail_rec(2**1000))
print(decimal_to_binary_gen(2**1000))
