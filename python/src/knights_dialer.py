from common import time_execution
import numpy as np

leads_to = [(4, 6), (8, 6), (7, 9), (4, 8), (3, 9, 0),
            (), (1, 7, 0), (2, 6), (1, 3), (4, 2)]


@time_execution()
def count_paths_dp_np(digit: int, hops: int) -> int:
    dp = np.zeros((10, hops+1), int)
    dp[:, 0] = 1  # 1 way to be at each digit with 0 hops

    for h in range(1, hops + 1):
        for d in range(10):
            # 'd' can be reached from any digit that it leads to (they also lead back to 'd')
            for nxt in leads_to[d]:  # sum of ways to get to those digits with 1 less hop
                dp[d, h] += dp[nxt, h - 1]

    return dp[digit, hops]


@time_execution()
def count_paths_dp(digit: int, hops: int) -> int:
    dp = [[0 for _ in range(hops + 1)] for _ in range(10)]

    # 1 way to be at each digit with 0 hops
    for d in range(10):
        dp[d][0] = 1

    for h in range(1, hops + 1):
        for d in range(10):
            # 'd' can be reached from any digit that it leads to (they also lead back to 'd')
            for nxt in leads_to[d]:  # sum of ways to get to those digits with 1 less hop
                dp[d][h] += dp[nxt][h - 1]

    return dp[digit][hops]


@time_execution()
def count_paths(digit: int, hops: int) -> int:
    def helper(digit: int, hops: int) -> int:
        if hops == 0:
            return 1
        count = 0
        for d in leads_to[digit]:
            count += helper(d, hops-1)

        return count

    return helper(digit, hops)


@time_execution()
def count_paths_memo(digit: int, hops: int) -> int:
    memo = {}

    def helper(digit: int, hops: int) -> int:
        key = (digit, hops)
        if key in memo:
            return memo[key]
        if hops == 0:
            return 1
        count = 0
        for d in leads_to[digit]:
            count += helper(d, hops-1)

        memo[key] = count
        return count

    return helper(digit, hops)


print(count_paths_dp(4, 15))
print(count_paths_dp_np(4, 15))
print(count_paths(4, 15))
print(count_paths_memo(4, 15))
