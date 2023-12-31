import sys
from functools import reduce
from operator import mul
from common import time_execution


@time_execution()
def fact_iter(n: int) -> int:
    return reduce(mul, [num for num in range(1, n+1)])


@time_execution()
def fact_rec(n: int) -> int:
    def helper(n: int):
        return 1 if n == 1 else n*helper(n-1)
    return helper(n)


@time_execution()
def fact_tail_rec(n: int) -> int:
    def helper(n: int, acc: int = 1) -> int:
        return acc if n == 1 else helper(n-1, n*acc)
    return helper(n)


@time_execution(isTrampoline=True)
def fact_tail_gen(n: int) -> int:
    def helper(n: int, acc: int = 1) -> int:
        yield acc if n == 1 else helper(n-1, n*acc)
    return helper(n)


print(fact_iter(100))
print(fact_rec(100))
print(fact_tail_rec(100))

sys.set_int_max_str_digits(100_000)
print(fact_tail_gen(10_000))
