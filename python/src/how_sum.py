# Return a combination of any elements that add up to target_sum
from common import time_execution


@time_execution
def how_sum_tabulation(target_sum: int, numbers: list[int]) -> list[int] | None:
    table = [None]*(target_sum+1)
    table[0] = []  # Base case

    for i in range(target_sum+1):
        if table[i] is not None:  # [] or contains some numbers
            for num in numbers:
                if i+num == target_sum:  # Found a solution
                    return table[i+num]
                if i+num < target_sum:  # Still smaller
                    table[i+num] = table[i] + [num]
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
            if (res := helper(remainder)) is not None:
                return [num] + res

        return None

    return helper(target_sum)


@time_execution
def how_sum_rec_memo(target_sum: int, numbers: list[int]) -> list[int] | None:
    memo = {0: []}

    # memo_count = 0

    def helper(target_sum: int):
        # nonlocal memo_count

        if target_sum in memo:
            # memo_count += 1
            return memo[target_sum]
        if target_sum < 0:
            return None

        for num in numbers:
            remainder = target_sum - num
            if (res := helper(remainder)) is not None:
                memo[target_sum] = [num] + res
                return memo[target_sum]

        memo[target_sum] = None
        return None

    return helper(target_sum)
    return f"Res: {helper(target_sum)}, memo_count: {memo_count}\n"


@time_execution
def how_sum_rec_v2(target_sum: int, numbers: list[int]) -> list[int] | None:
    nums_len = len(numbers)

    def helper(idx: int, sum_so_far=0):
        if sum_so_far == target_sum:
            return []
        if sum_so_far > target_sum or idx == nums_len:
            return None

        if (res := helper(idx, sum_so_far+numbers[idx])) is not None:
            return [numbers[idx]] + res
        if (res := helper(idx+1, sum_so_far)) is not None:
            return res

    return helper(0)


@time_execution
def how_sum_rec_v2_memo(target_sum: int, numbers: list[int]) -> list[int]:
    nums_len = len(numbers)
    memo = {target_sum: []}

    # memo_count = 0

    def helper(idx: int, sum_so_far=0):
        # nonlocal memo_count
        key = sum_so_far

        if key in memo:
            # memo_count += 1
            return memo[key]

        if sum_so_far > target_sum or idx == nums_len:
            return None

        if (res := helper(idx, sum_so_far + numbers[idx])) is not None:
            memo[key] = [numbers[idx]] + res
            return memo[key]

        if (res := helper(idx + 1, sum_so_far)) is not None:
            memo[key] = res
            return memo[key]

        memo[key] = None
        return None

    return helper(0)
    return f"Res: {helper(0)}, memo_count: {memo_count}\n"


print(how_sum_tabulation(300, [7, 14]))
# print(how_sum_rec(300, [7, 14]))
print(how_sum_rec_memo(300, [7, 14]))
print(how_sum_rec_v2(300, [7, 14]))
print(how_sum_rec_v2_memo(300, [7, 14]))
