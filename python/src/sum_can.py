# Check if it's possible to generate the target sum using numbers from the array
# all input numbers are non negative and can be used more than once
from common import time_execution


@time_execution()
def can_sum_tabulation(target_sum: int, numbers: list[int]) -> bool:
    table = [False] * (target_sum + 1)  # Worstcase length sum of 1's
    table[0] = True  # Base case, but also enables us to pass the if later
    for i in range(target_sum + 1):
        if table[i]:
            for num in numbers:
                # Found a combination and can immediately exit
                if i + num == target_sum:
                    return True
                # We can add more to that position next time since still smaller
                if i + num < target_sum:
                    table[i + num] = True

    return False


@time_execution()
def can_sum_iter(target_sum: int, numbers: list[int]) -> bool:
    sums_so_far = [0]

    while sums_so_far:
        new_sums = set()
        for sum_so_far in sums_so_far:
            for num in numbers:
                curr_sum = num + sum_so_far
                if curr_sum == target_sum:  # Found a way to get target_sum
                    return True
                if curr_sum < target_sum:  # Sum still smaller so add it
                    new_sums.add(curr_sum)
        sums_so_far = new_sums

    return False


@time_execution()
def can_sum_rec(target_sum: int, numbers: list[int]) -> bool:
    def helper(idx: int, acc=0):
        if idx == len(numbers) or acc > target_sum:
            return False
        if acc == target_sum:
            return True
        return helper(idx, acc+numbers[idx]) or helper(idx+1, acc)

    return helper(0)


@time_execution()
def can_sum_memo(target_sum: int, numbers: list[int]) -> bool:
    memo = {}
    memo_count = 0

    def helper(idx: int, acc=0) -> bool:
        nonlocal memo_count
        if (idx, acc) in memo:
            memo_count += 1
            return memo[idx, acc]
        if idx == len(numbers) or acc > target_sum:
            return False
        if acc == target_sum:
            return True

        memo[idx, acc] = helper(idx, acc+numbers[idx]) or helper(idx+1, acc)
        return memo[idx, acc]

    return f"Res: {helper(0)}, memo_count: {memo_count}"


@time_execution()
def can_sum_rec_v2(target_sum: int, numbers: list[int]) -> bool:
    def helper(remainder: int) -> bool:
        if remainder == 0:
            return True
        if remainder < 0:
            return False
        for num in numbers:
            if helper(remainder-num):
                return True

        return False
    return helper(target_sum)


@time_execution()
def can_sum_memo_v2(target_sum: int, numbers: list[int]) -> bool:
    memo = {0: True}
    memo_count = 0

    def helper(remainder: int) -> bool:
        nonlocal memo_count

        if remainder in memo:
            memo_count += 1
            return memo[remainder]
        if remainder < 0:
            return False

        for num in numbers:
            if helper(remainder-num):
                memo[remainder] = True
                return True

        memo[remainder] = False
        return False

    return f"Res: {helper(target_sum)}, memo_count: {memo_count}"


print(can_sum_tabulation(900, [7, 14, 28]))
print(can_sum_iter(900, [7, 14, 28]))
print(can_sum_rec(900, [7, 14, 28]))
print(can_sum_memo(900, [7, 14, 28]))
# print(can_sum_rec_v2(900, [7, 14, 28]))
print(can_sum_memo_v2(900, [7, 14, 28]))
