import sys
from common import tramp


def fibonacci_iter(n: int) -> int:
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2, n+1):
            a, b = b, a+b
        return b


def fibonacci_rec(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)


def fibonacci_tail_rec(n: int, curr=0, nxt=1) -> int:
    if n == 0:
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
print([fibonacci_tail_rec(i) for i in range(10)])
sys.set_int_max_str_digits(20899)
print(tramp(fibonacci_gen, 100_000))
