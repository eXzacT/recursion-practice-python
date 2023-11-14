# Sum of first n numbers

def calculate_sum(n: int) -> int:
    return n*(n+1)/2


def sum_rec(n: int) -> int:
    if n == 0:
        return n
    return n+sum_rec(n-1)


def sum_tail_rec(n: int, acc=0) -> int:
    if n == 0:
        return acc
    return sum_tail_rec(n-1, acc+n)


def sum_rec_gen(n: int, acc=0) -> int:
    if n == 0:
        yield acc
    yield sum_rec_gen(n-1, acc+n)
