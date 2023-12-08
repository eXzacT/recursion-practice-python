import sys
from common import tramp, time_execution


@time_execution()
def fibonacci_iter(n: int) -> int:
    a = 0
    b = 1

    if n <= 0:
        return 0
    if n == 1:
        return 1

    for _ in range(n-1):
        a, b = b, a+b
    return b


@time_execution()
def fibonacci_tabulation(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1

    table = [0]*(n+1)
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1]+table[i-2]

    return table[-1]


@time_execution()
def fibonacci_rec(n: int) -> int:
    if n < 0:
        return 0

    def helper(n: int) -> int:
        if n <= 1:
            return n
        return helper(n-1) + helper(n-2)
    return helper(n)


@time_execution()
def fibonacci_memo(n: int) -> int:
    memo = {0: 0, 1: 1}
    if n < 0:
        return 0

    def helper(n: int) -> int:
        if n in memo:
            return memo[n]
        memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
        return memo[n]
    return helper(n)


@time_execution()
def fibonacci_tail_rec(n: int) -> int:
    def helper(n: int, curr=0, nxt=1):
        if n <= 0:
            return curr
        else:
            return helper(n-1, nxt, curr+nxt)
    return helper(n)


@time_execution(isTrampoline=True)
def fibonacci_gen(n: int) -> int:
    def helper(n: int, curr=0, nxt=1):
        if n == 0:
            yield curr
        else:
            yield helper(n-1, nxt, curr+nxt)
    return helper(n)


print(fibonacci_iter(10))
print(fibonacci_tabulation(10))
print(fibonacci_rec(10))
print(fibonacci_tail_rec(10))

sys.set_int_max_str_digits(20899)
print(tramp(fibonacci_gen, 100_000))
