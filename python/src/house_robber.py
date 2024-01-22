'''
Given a list of houses with their values and a constraint of not being able to rob 2 houses in a row.
What's the most money a robber can get?
'''
from common import time_execution


@time_execution()
def house_robber_dp(values: list[int]) -> int:
    if len(values) == 1:  # If there's only 1 house to rob
        return values[0]

    dp = [0]*len(values)
    dp[0] = values[0]  # Max we can rob at first house is the first house itself
    # Max we can rob at the second house is max between first and second
    dp[1] = max(values[0], values[1])

    # At every position max we can rob so far is either the values we got during previous house, OR
    # 2 houses ago + value of current house
    for i in range(2, len(values)):
        dp[i] = max(dp[i-2]+values[i], dp[i-1])

    return dp[-1]


@time_execution()
def house_robber_dp_v2(values: list[int]) -> int:
    if len(values) == 1:  # If there's only 1 house to rob
        return values[0]

    prevprev = values[0]
    prev = max(values[0], values[1])

    # At any point we only store previous and 2 houses ago max values
    for i in range(2, len(values)):
        # prevprev becomes prev and prev becomes the max between them(for prevprev we can add current house)
        prevprev, prev = prev, max(prevprev+values[i], prev)

    return prev


@time_execution()
def house_robber_rec(values: list[int]) -> int:
    def rob(idx: int = 0) -> int:
        if idx >= len(values):
            return 0
        return max(values[idx]+rob(idx+2), rob(idx+1))

    return rob()


@time_execution()
def house_robber_memo(values: list[int]) -> int:
    memo = {}
    memo_hits = 0

    def rob(idx: int = 0) -> int:
        nonlocal memo_hits
        if idx in memo:
            memo_hits += 1
            return memo[idx]
        if idx >= len(values):
            return 0
        memo[idx] = max(values[idx]+rob(idx+2), rob(idx+1))
        return memo[idx]

    return f"{rob()}, memo_hits: {memo_hits}"


values = [5, 6, 4, 3, 6, 2, 1, 7, 9, 20, 1, 4, 5]
print(house_robber_dp(values))
print(house_robber_dp_v2(values))
print(house_robber_rec(values))
print(house_robber_memo(values))
