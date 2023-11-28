# Return a combination of any elements that add up to target_sum
from common import time_execution


@time_execution
def how_sum_iter(target_sum: int, numbers: list[int]) -> list[int] | None:
    dp = [None]*(target_sum+1)
    dp[0] = []

    for i in range(target_sum+1):
        if dp[i] is not None:
            for num in numbers:
                if i+num <= target_sum:
                    dp[i+num] = dp[i] + [num]
                    if i+num == target_sum:
                        return dp[i+num]
    return None


@time_execution
def how_sum_rec(target_sum: int, numbers: list[int]) -> list[int] | None:
    def helper(target_sum: int):
        if target_sum == 0:
            return []
        if target_sum < 0:
            return None

        for num in numbers:
            remainder = target_sum - num
            result = helper(remainder)
            if result:
                return [num] + result

        return None

    return helper(target_sum)


@time_execution
def how_sum_rec_memo(target_sum: int, numbers: list[int]) -> list[int] | None:
    memo = {}

    def helper(target_sum: int):
        if target_sum in memo:
            return memo[target_sum]
        if target_sum == 0:
            return []
        if target_sum < 0:
            return None

        for num in numbers:
            remainder = target_sum - num
            result = helper(remainder)
            if result:
                memo[target_sum] = [num] + result
                return memo[target_sum]

        memo[target_sum] = None
        return None

    return helper(target_sum)


@time_execution
def how_sum_rec_v2(target_sum: int, numbers: list[int]) -> list[int] | None:
    nums_len = len(numbers)

    def helper(idx: int, sum_so_far=0):
        if sum_so_far == target_sum:
            return []
        if sum_so_far > target_sum or idx == nums_len:
            return None

        if (res := helper(idx, sum_so_far+numbers[idx])):
            return [numbers[idx]] + res

        if (res := helper(idx+1, sum_so_far)):
            return res

    return helper(0)


@time_execution
def how_sum_rec_v2_memo(target_sum: int, numbers: list[int]) -> list[int] | None:
    nums_len = len(numbers)
    memo = {}

    def helper(idx: int, sum_so_far=0):
        if (idx, sum_so_far) in memo:
            return memo[(idx, sum_so_far)]
        if sum_so_far == target_sum:
            return []
        if sum_so_far > target_sum or idx == nums_len:
            return None

        if (res := helper(idx, sum_so_far+numbers[idx])):
            memo[(idx, sum_so_far)] = [numbers[idx]] + res
            return memo[(idx, sum_so_far)]

        if (res := helper(idx+1, sum_so_far)):
            memo[(idx, sum_so_far)] = res
            return memo[(idx, sum_so_far)]

        return None

    return helper(0)


@time_execution
def how_sum_rec_v2_memo(target_sum: int, numbers: list[int]) -> list[int]:
    nums_len = len(numbers)
    memo = {}

    def helper(idx: int, sum_so_far=0):
        if (idx, sum_so_far) in memo:
            return memo[(idx, sum_so_far)]
        if sum_so_far == target_sum:
            return []
        if sum_so_far > target_sum or idx == nums_len:
            return None

        if (res := helper(idx, sum_so_far + numbers[idx])):
            memo[(idx, sum_so_far)] = [numbers[idx]] + res
            return memo[(idx, sum_so_far)]

        if (res := helper(idx + 1, sum_so_far)):
            memo[(idx, sum_so_far)] = res
            return memo[(idx, sum_so_far)]

        memo[(idx, sum_so_far)] = None
        return None

    return helper(0)


print(how_sum_iter(300, [7, 14]))
# print(how_sum_rec(300, [7, 14]))
print(how_sum_rec_memo(300, [7, 14]))
print(how_sum_rec_v2(300, [7, 14]))
print(how_sum_rec_v2_memo(300, [7, 14]))
