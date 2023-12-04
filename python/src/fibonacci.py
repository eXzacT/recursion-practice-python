import sys
from common import tramp


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


def fibonacci_tabulation(n: int) -> list[int]:
    if n <= 0:
        return [0]
    if n == 1:
        return [1]

    table = [0]*(n+1)
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1]+table[i-2]

    return table


def fibonacci_rec(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)


def fibonacci_memo(n: int, memo={}) -> int:
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]


def fibonacci_tail_rec(n: int, curr=0, nxt=1) -> int:
    if n <= 0:
        return curr
    else:
        return fibonacci_tail_rec(n-1, nxt, curr+nxt)


def fibonacci_gen(n: int, curr=0, nxt=1) -> int:
    if n == 0:
        yield curr
    else:
        yield fibonacci_gen(n-1, nxt, curr+nxt)


print([fibonacci_iter(i) for i in range(10)])
print([fibonacci_rec(i) for i in range(10)])
print([fibonacci_memo(i) for i in range(10)])
print([fibonacci_tail_rec(i) for i in range(10)])

sys.set_int_max_str_digits(20899)
print(tramp(fibonacci_gen, 100_000))
