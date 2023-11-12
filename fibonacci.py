import sys
from common import tramp


def fibonacci_iterative(n: int) -> int:
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


def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_recursive_tail(n: int, curr=0, nxt=1) -> int:
    if n == 0:
        return curr
    else:
        return fibonacci_recursive_tail(n-1, nxt, curr+nxt)


def fibonacci_recursive_tail_gen(n: int, curr=0, nxt=1) -> int:
    if n == 0:
        yield curr
    else:
        yield fibonacci_recursive_tail_gen(n-1, nxt, curr+nxt)


print([fibonacci_recursive_tail(i) for i in range(10)])
print([tramp(fibonacci_recursive_tail_gen, i) for i in range(10)])
print([fibonacci_recursive(i) for i in range(10)])

# sys.set_int_max_str_digits(20899)
# print(tramp(fibonacci_recursive_tail_gen, 100_000))
# With this approach we are creating a generator from a generator (08/11/2023)
# fibonacci_gen = (tramp(fibonacci_recursive_tail_gen, i)
#                      for i in range(100_000))
# for fibonacci in fibonacci_gen:
#     print(fibonacci)
