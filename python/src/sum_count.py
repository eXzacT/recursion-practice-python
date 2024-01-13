from common import time_execution


@time_execution()
def count_sum_dp(target_sum: int, numbers: list) -> int:
    dp = [0] * (target_sum + 1)
    dp[0] = 1  # There is one way to make zero (with no numbers)
    for num in numbers:
        # To get from 7 to 10, we can for example add 3
        # So for all ways that we can construct 7, we can also add 3 and get to 10
        for n in range(num, target_sum + 1):
            dp[n] += dp[n - num]

    return dp[-1]


@time_execution()
def count_sum(target_sum: int, numbers: list[int]) -> int:
    def helper(idx: int, sum_so_far: int = 0) -> int:
        if sum_so_far == target_sum:
            return 1
        if idx == len(numbers) or sum_so_far > target_sum:
            return 0

        return helper(idx, sum_so_far+numbers[idx]) + helper(idx+1, sum_so_far)

    return helper(0)


@time_execution()
def count_sum_memo(target_sum: int, numbers: list[int]) -> int:
    memo = {target_sum: 1}
    memo_count = 0

    def helper(idx: int, sum_so_far: int = 0) -> int:
        nonlocal memo_count
        key = (sum_so_far, idx)

        if sum_so_far == target_sum:
            return 1
        if key in memo:
            memo_count += 1
            return memo[key]
        if idx == len(numbers) or sum_so_far > target_sum:
            return 0

        memo[key] = helper(
            idx, sum_so_far+numbers[idx]) + helper(idx+1, sum_so_far)
        return memo[key]

    return f"{helper(0)}, {memo_count} memo lookups"


@time_execution()
def count_sum_v2(target_sum: int, numbers: list) -> int:
    def helper(sum_so_far: int, last_used_index: int) -> int:
        if sum_so_far == target_sum:
            return 1
        if sum_so_far > target_sum:
            return 0

        count = 0
        # Only consider numbers at or after the last used index to prevent permutations of the same combination
        for i in range(last_used_index, len(numbers)):
            count += helper(sum_so_far + numbers[i], i)

        return count

    return helper(0, 0)


@time_execution()
def count_sum_v2_memo(target_sum: int, numbers: list) -> int:
    memo = {}
    memo_count = 0

    def helper(sum_so_far: int, last_used_index: int) -> int:
        nonlocal memo_count
        key = (sum_so_far, last_used_index)

        if sum_so_far == target_sum:
            return 1
        if key in memo:
            memo_count += 1
            return memo[key]
        if sum_so_far > target_sum:
            return 0

        count = 0
        # Only consider numbers at or after the last used index to prevent permutations of the same combination
        for i in range(last_used_index, len(numbers)):
            count += helper(sum_so_far + numbers[i], i)

        memo[key] = count
        return count

    return f"{helper(0, 0)}, {memo_count} memo lookups"


print(count_sum_dp(35, [1, 2, 3]))
print(count_sum(35, [1, 2, 3]))
print(count_sum_memo(35, [1, 2, 3]))
print(count_sum_v2(35, [1, 2, 3]))
print(count_sum_v2_memo(35, [1, 2, 3]))
