def calculate_sum(n: int) -> int:
    return n*(n+1)/2


def sum_recursive(n: int) -> int:
    if n == 0:
        return n
    return n+sum_recursive(n-1)


def sum_recursive_tail(n: int, accumulator: int = 0) -> int:
    if n == 0:
        return accumulator
    return sum_recursive_tail(n-1, accumulator+n)


def sum_recursive_tail_gen(n: int, accumulator: int = 0) -> int:
    if n == 0:
        yield accumulator
    yield sum_recursive_tail_gen(n-1, accumulator+n)
