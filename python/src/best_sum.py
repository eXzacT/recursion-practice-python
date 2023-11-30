# Return the shortest combination of any elements that add up to target_sum
from common import time_execution


@time_execution
def best_sum_tabulation(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []

    for i in range(target_sum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target_sum:
                    combination = [num] + table[i]
                    if not table[i + num] or len(combination) < len(table[i + num]):
                        table[i + num] = combination

    return table[target_sum]


def best_sum_rec(target_sum: int, numbers: list[int]) -> list[int]:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None

    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum_rec(remainder, numbers)

        if remainder_combination is not None:
            combination = remainder_combination + [num]
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    return shortest_combination


@time_execution
def best_sum_rec_memo(target_sum: int, numbers: list[int]) -> list[int]:
    memo = {0: []}

    def helper(target: int):
        if target in memo:
            return memo[target]
        if target < 0:
            return None

        shortest_combination = None

        for num in numbers:
            remainder = target-num
            if (remainder_combination := helper(remainder)) is not None:
                combination = remainder_combination + [num]
                if shortest_combination is None \
                        or len(combination) < len(shortest_combination):
                    shortest_combination = combination

        memo[target] = shortest_combination
        return memo[target]

    return helper(target_sum)


@time_execution
def best_sum_rec_v2(target_sum: int, numbers: list[int]) -> list[int] | None:
    nums_len = len(numbers)
    results = []

    def helper(remaining: int, idx=0, nums_so_far=[]):

        if remaining == 0:
            return nums_so_far
        if remaining < 0 or idx == nums_len:
            return None

        with_num = helper(
            remaining - numbers[idx], idx, [numbers[idx]]+nums_so_far)
        if with_num is not None:
            results.append(with_num)

        helper(remaining, idx + 1, nums_so_far)

    helper(target_sum)
    return min(results, key=len) if results else None


@time_execution
def best_sum_rec_v2_memo(target_sum: int, numbers: list[int]) -> list[int] | None:
    memo = {}

    def helper(remaining: int, idx=0):
        if (remaining, idx) in memo:
            return memo[(remaining, idx)]
        if remaining == 0:
            return []
        if remaining < 0 or idx == len(numbers):
            return None

        with_num = helper(remaining - numbers[idx], idx)
        if with_num is not None:
            with_num = with_num+[numbers[idx]]

        without_num = helper(remaining, idx + 1)

        if with_num is None or (without_num is not None and len(without_num) < len(with_num)):
            memo[(remaining, idx)] = without_num
        else:
            memo[(remaining, idx)] = with_num

        return memo[(remaining, idx)]

    return helper(target_sum)


print(best_sum_tabulation(35, [1, 2, 3]))
# print(best_sum_rec(10, [1, 2, 3]))
print(best_sum_rec_memo(35, [1, 2, 3]))
print(best_sum_rec_v2(35, [1, 2, 3]))
print(best_sum_rec_v2_memo(35, [1, 2, 3]))
