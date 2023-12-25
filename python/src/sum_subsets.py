# Print sums of all subsets of a given set
from itertools import combinations
from common import time_execution


@time_execution()
def sum_subsets(arr: list[int]) -> list[int]:
    return [sum([arr[j] for j in range(len(arr)) if i & (
        1 << j)]) for i in range(1 << len(arr))]


@time_execution()
def sum_subsets_rec(arr: list[int]):
    sums = []

    def helper(idx: int, subset_sum=0):
        if idx == len(arr):
            sums.append(subset_sum)
        else:
            helper(idx + 1, subset_sum + arr[idx])
            helper(idx + 1, subset_sum)

    helper(0)
    return sums


arr = [2, 4, 9, 1, 2, 10]
print(sum_subsets(arr))
print(sum_subsets_rec(arr))

# Bonus
print([sum(comb) for i in range(len(arr) + 1)
      for comb in combinations(arr, i)])
