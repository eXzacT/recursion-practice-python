# Find m-th summation of first n natural numbers

def natural_nums_summation_iter(m: int, n: int) -> int:
    for _ in range(1, m+1):
        nums_sum = 0
        for j in range(1, n+1):
            nums_sum += j
        n = nums_sum
    return n


def natural_nums_summation_rec(m: int, n: int) -> int:
    if m == 0:
        return n
    n = sum(range(1, n+1))

    return natural_nums_summation_rec(m-1, n)


def natural_nums_summation_rec_v3(m: int, n: int):
    if m == 1:
        return (n * (n + 1) // 2)
    sum_nums = natural_nums_summation_rec_v3(m - 1, n)
    return (sum_nums * (sum_nums + 1) // 2)


print(natural_nums_summation_iter(4, 5))
print(natural_nums_summation_rec(4, 5))
print(natural_nums_summation_rec_v3(4, 5))
