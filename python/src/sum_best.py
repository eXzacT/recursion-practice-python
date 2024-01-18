# Return the shortest combination of any elements that add up to target_sum
from common import time_execution


@time_execution()
def best_sum_dp(target_sum, numbers):
    dp = [None] * (target_sum + 1)
    dp[0] = []  # Base case

    for i in range(target_sum + 1):
        if dp[i] is not None:
            for num in numbers:
                if i + num <= target_sum:
                    # If that entry doesn't exist yet or we found a shorter combination
                    if not dp[i+num] or len(dp[i])+1 < len(dp[i+num]):
                        dp[i+num] = [num]+dp[i]

    return dp[target_sum]


@time_execution()
def best_sum_rec(target_sum: int, numbers: list[int]) -> list[int]:
    def helper(target_sum: int) -> list[int]:
        if target_sum == 0:
            return []
        if target_sum < 0:
            return None

        shortest_combination = None

        for num in numbers:
            remainder = target_sum - num
            remainder_combination = helper(remainder)

            if remainder_combination is not None:
                combination = remainder_combination + [num]
                if shortest_combination is None or len(combination) < len(shortest_combination):
                    shortest_combination = combination

        return shortest_combination

    return helper(target_sum)


@time_execution()
def best_sum_rec_memo(target_sum: int, numbers: list[int]) -> list[int]:
    memo = {0: []}
    memo_count = 0

    def helper(target: int):
        nonlocal memo_count

        if target in memo:
            memo_count += 1
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

    return f"{helper(target_sum)}, memo count: {memo_count}"


@time_execution()
def best_sum_rec_v2(target_sum: int, numbers: list[int]) -> list[int] | None:
    shortest_combination = None

    def helper(target: int, idx=0, nums_so_far=[]):
        nonlocal shortest_combination
        if target < 0 or idx == len(numbers):
            return None
        if target == 0:
            return nums_so_far

        # # Return early if we already have more elements in the combination
        if shortest_combination and len(nums_so_far) > len(shortest_combination):
            return None

        combination = helper(
            target - numbers[idx], idx, [numbers[idx]]+nums_so_far)
        if combination is not None:
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

        helper(target, idx + 1, nums_so_far)

    helper(target_sum)
    return shortest_combination


@time_execution()
def best_sum_rec_v2_memo(target_sum: int, numbers: list[int]) -> list[int] | None:
    memo = {0: []}
    memo_count = 0

    def helper(target: int, idx=0):
        nonlocal memo_count
        key = target

        if key in memo:
            memo_count += 1
            return memo[key]
        if target < 0 or idx == len(numbers):
            return None

        with_num = helper(target - numbers[idx], idx)
        if with_num is not None:
            with_num = with_num+[numbers[idx]]

        without_num = helper(target, idx + 1)

        if with_num is None or (without_num is not None and len(without_num) < len(with_num)):
            memo[key] = without_num
        else:
            memo[key] = with_num

        return memo[key]

    return f"{helper(target_sum)}, memo count: {memo_count}"


print(best_sum_dp(35, [1, 2, 3]))
# print(best_sum_rec(35, [1, 2, 3]))
print(best_sum_rec_memo(35, [1, 2, 3]))
print(best_sum_rec_v2(35, [1, 2, 3]))
print(best_sum_rec_v2_memo(35, [1, 2, 3]))
