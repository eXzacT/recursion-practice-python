# Sum of first n numbers
from common import time_execution


@time_execution()
def sum_formula(n: int) -> int:
    return n*(n+1)/2


@time_execution()
def sum_rec(n: int) -> int:
    def helper(n: int) -> int:
        if n == 0:
            return n
        return n+helper(n-1)
    return helper(n)


@time_execution()
def sum_tail_rec(n: int) -> int:
    def helper(n: int, acc=0) -> int:
        if n == 0:
            return acc
        return helper(n-1, acc+n)
    return helper(n)


@time_execution(isTrampoline=True)
def sum_gen(n: int) -> int:
    def helper(n: int, acc=0) -> int:
        if n == 0:
            yield acc
        yield helper(n-1, acc+n)
    return helper(n)


print(sum_formula(35))
print(sum_rec(35))
print(sum_tail_rec(35))
print(sum_gen(100_000))
