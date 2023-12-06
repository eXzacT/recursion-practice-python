# Find m-th summation of first n natural numbers
# Basically sum of first n numbers, then keep extending it by the last result
# 1 to inc. 5 = 15 -> then 1 to incl. 15
from common import time_execution


@time_execution
def natural_nums_summation_formula(m: int, n: int) -> int:
    for _ in range(m):
        n = n*(n+1)//2
    return n


@time_execution
def natural_nums_summation_rec_formula(m: int, n: int):
    def helper(m: int):
        if m == 1:
            return (n * (n + 1) // 2)
        sum_nums = helper(m - 1)
        return (sum_nums * (sum_nums + 1) // 2)
    return helper(m)


@time_execution
def natural_nums_summation_iter(m: int, n: int) -> int:
    for _ in range(m):
        n = sum(range(1, n+1))
    return n


@time_execution
def natural_nums_summation_rec(m: int, n: int) -> int:
    def helper(m: int, n: int):
        if m == 0:
            return n
        n = sum(range(1, n+1))
        return helper(m-1, n)
    return helper(m, n)


@time_execution
def natural_nums_summation_tabulation(m: int, n: int) -> int:
    table = [0]
    for _ in range(m):
        while len(table) <= n:
            # This gives us next summation
            table.append(table[-1] + len(table))
        n = table[n]

    return n


@time_execution
def natural_nums_summation_tabulation_v2(m: int, n: int) -> int:
    table = [0]
    start = 1

    for _ in range(m):
        sum_so_far = table[-1]
        table.append(sum_so_far+sum(range(start, n+1)))
        start = n+1
        n = table[-1]

    return n


print(natural_nums_summation_formula(4, 5))
print(natural_nums_summation_rec_formula(4, 5))
print(natural_nums_summation_iter(4, 5))
print(natural_nums_summation_rec(4, 5))
print(natural_nums_summation_tabulation(4, 5))
print(natural_nums_summation_tabulation_v2(4, 5))
