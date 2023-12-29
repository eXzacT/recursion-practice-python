from itertools import permutations
from common import time_execution


@time_execution()
def permutations_of_first_n(n: int) -> list[int]:
    permutations = []

    def helper(nums: list, permutation: list = []) -> None:
        if len(permutation) == n:
            permutations.append(permutation)
            return

        for i in range(len(nums)):
            helper(nums[:i] + nums[i+1:], permutation + [nums[i]])

    helper([num for num in range(1, n+1)])
    return permutations


@time_execution()
def heaps_algorithm(n: int) -> list:
    permutations = []

    def helper(idx: int, nums: list) -> None:
        if idx == 1:
            permutations.append(nums.copy())
        else:
            for i in range(idx-1):
                helper(idx-1, nums)
                if idx % 2 == 0:
                    nums[i], nums[idx-1] = nums[idx-1], nums[i]
                else:
                    nums[0], nums[idx-1] = nums[idx-1], nums[0]
            helper(idx-1, nums)

    helper(n, [num for num in range(1, n+1)])
    return permutations


print(permutations_of_first_n(3))
print(heaps_algorithm(3))

# Bonus(heaps algorithm under the hood)
print(list(permutations(range(1, 3+1))))
