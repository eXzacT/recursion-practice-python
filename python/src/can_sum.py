# Check if it's possible to generate the target sum using numbers from the array
# all input numbers are non negative and can be used more than once

def can_sum_iter(target_sum: int, numbers: list[int]) -> bool:
    dp = [False] * (target_sum + 1)
    dp[0] = True

    for i in range(target_sum + 1):
        if dp[i]:
            for num in numbers:
                if i + num == target_sum:
                    return True
                if i + num < target_sum:
                    dp[i + num] = True

    return False


def can_sum_iter_v2(target_sum: int, numbers: list[int]) -> bool:
    sums_so_far = set([0])

    for num in numbers:
        new_sums = set()
        for sm in sums_so_far:
            curr_sum = num+sm
            if curr_sum == target_sum:
                return True
            if curr_sum < target_sum:
                new_sums.add(curr_sum)
        sums_so_far.update(new_sums)

    return False


def can_sum_rec(target_sum: int, numbers: list[int]) -> bool:
    nums_len = len(numbers)

    def helper(idx: int, acc=0):
        if idx == nums_len or acc > target_sum:
            return False
        if acc == target_sum:
            return True
        return helper(idx, acc+numbers[idx]) or helper(idx+1, acc)
    return helper(0)


def can_sum_memo(target_sum: int, numbers: list[int]) -> bool:
    nums_len = len(numbers)
    memo = {}

    def helper(idx: int, acc=0) -> bool:
        if (idx, acc) in memo:
            return memo[idx, acc]
        if idx == nums_len or acc > target_sum:
            return False
        if acc == target_sum:
            return True

        memo[idx, acc] = helper(idx, acc+numbers[idx]) or helper(idx+1, acc)
        return memo[idx, acc]

    return helper(0)


def can_sum_rec_v2(target_sum: int, numbers: list[int]) -> bool:
    def helper(target_sum: int) -> bool:
        if target_sum == 0:
            return True
        if target_sum < 0:
            return False
        for num in numbers:
            if helper(target_sum-num):
                return True

        return False
    return helper(target_sum)


def can_sum_memo_v2(target_sum: int, numbers: list[int]) -> bool:
    memo = {}

    def helper(target_sum: int) -> bool:
        if target_sum in memo:
            return memo[target_sum]
        if target_sum == 0:
            return True
        if target_sum < 0:
            return False
        for num in numbers:
            if helper(target_sum-num):
                memo[target_sum] = True
                return True

        memo[target_sum] = False
        return False

    return helper(target_sum)


print(can_sum_iter(1000, [num for num in range(1, 50)]))
print(can_sum_iter(57, [5, 50]))
print(can_sum_iter_v2(1000, [num for num in range(1, 50)]))
print(can_sum_iter_v2(57, [5, 50]))

print(can_sum_rec(900, [7, 14, 28]))
print(can_sum_memo(900, [7, 14, 28]))
print(can_sum_rec_v2(900, [7, 14, 28]))
print(can_sum_memo_v2(900, [7, 14, 28]))
