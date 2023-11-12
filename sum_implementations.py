def calculate_sum(n: int) -> int:
    return n*(n+1)/2


def sum_recursive(n: int) -> int:
    if n == 0:
        return n
    return n+sum_recursive(n-1)


def sum_recursive_tail(n: int, acc: int = 0) -> int:
    if n == 0:
        return acc
    return sum_recursive_tail(n-1, acc+n)


def sum_recursive_tail_gen(n: int, acc: int = 0) -> int:
    if n == 0:
        yield acc
    yield sum_recursive_tail_gen(n-1, acc+n)
