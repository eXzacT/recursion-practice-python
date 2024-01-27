'''Given a target sum and a list of coins, what's the shortest combination that makes up to the target?'''
from common import time_execution


@time_execution()
def min_coins_dp(target: int, coins: list[int]) -> int:
    dp = [float("inf")]*(target+1)
    dp[0] = 0
    for curr_sum in range(target+1):
        # If we can actually sum to this number using the coins
        if dp[curr_sum] != float("inf"):
            for coin in coins:
                # If we didn't go out of bounds, get minimum ways to sum up to current sum
                if (new_sum := curr_sum+coin) <= target:
                    dp[new_sum] = min(dp[new_sum], 1+dp[curr_sum])

    return -1 if dp[-1] == float("inf") else dp[-1]


@time_execution()
def min_coins_dp_v2(target: int, coins: list[int]) -> int:
    dp = [False]*(target+1)
    dp[0] = 0
    for curr_sum in range(target+1):
        # If we can actually sum to this number using the coins
        if dp[curr_sum] or curr_sum == 0:
            for coin in coins:
                # If we didn't go out of bounds, get minimum ways to sum up to current sum
                if (new_sum := curr_sum+coin) <= target:
                    if dp[new_sum]:
                        dp[new_sum] = min(dp[new_sum], 1+dp[curr_sum])
                    else:
                        dp[new_sum] = 1+dp[curr_sum]

    return -1 if not dp[-1] else dp[-1]


@time_execution()
def min_coins_rec(target: int, coins: list[int]) -> int:
    def helper(remainder: int) -> int:
        if remainder == 0:
            return 0
        return min([1+helper(remainder-coin) for coin in coins if remainder-coin >= 0] or [float("inf")])

    min_coins = helper(target)
    return -1 if min_coins == float("inf") else min_coins


@time_execution()
def min_coins_memo(target: int, coins: list[int]) -> int:
    memo = {0: 0}

    def helper(remainder: int) -> int:
        if remainder in memo:
            return memo[remainder]
        memo[remainder] = min([1+helper(remainder-coin)
                              for coin in coins if remainder-coin >= 0] or [float('inf')])
        return memo[remainder]

    min_coins = helper(target)
    return -1 if min_coins == float("inf") else min_coins


print(min_coins_dp(15, [7, 3, 2]))
print(min_coins_dp_v2(15, [7, 3, 2]))
print(min_coins_rec(15, [7, 3, 2]))
print(min_coins_memo(15, [7, 3, 2]))
