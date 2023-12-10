# Printing 1 to n iteratively and recursively
from common import time_execution


@time_execution()
def one_to_n(n) -> list[int]:
    result = []

    def helper(start: int = 0) -> list[int]:
        if start > n:
            return
        result.append(start)
        return helper(start+1)
    helper()
    return result


@time_execution(isTrampoline=True)
def one_to_n_gen(n) -> list[int]:

    def helper(start=0, res=[]) -> list[int]:
        if start > n:
            yield res
        yield helper(start + 1, res+[start])
    return helper()


print(one_to_n(10))
# print(one_to_n(10000))
print(one_to_n_gen(10_000))
