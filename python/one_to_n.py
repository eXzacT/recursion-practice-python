# Print 1 to n without using loops
from common import tramp


def one_to_n(n, start=0):
    if start > n:
        return
    print(start)
    return one_to_n(n, start+1)


def one_to_n_gen(n):
    def helper(start=0):
        if start > n:
            yield
        print(start)
        yield helper(start + 1)
    return helper()


one_to_n(10)
# one_to_n(10000)
tramp(one_to_n_gen, 10_000)
