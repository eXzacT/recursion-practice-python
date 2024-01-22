'''Given a list of values, a list of weights with same index and a knapsack with a certain weight limit
    We can't take the same item more than once
    What's the total value we can store in a knapsack without exceeding its weight limit?
'''
from common import time_execution


@time_execution()
def knapsack_dp(values: list[int], weights: list[int], limit: int) -> int:
    if limit == 0:
        return 0
    if limit > sum(weights):
        return sum(values)

    WIDTH = limit+1
    HEIGHT = len(values)

    # First item value where the first item weight is less or equal to limit which is represented by idx
    # Example  [0,0,0,5,5,5,5] if item value is 5, weight 3 and limit is 6
    # Meaning with available weight of 3 and more we can use that item
    dp = [0]*WIDTH
    for i in range(weights[0], WIDTH):
        dp[i] = values[0]

    for i in range(1, HEIGHT):
        prev = dp.copy()
        for available_weight in range(WIDTH):
            item_weight = weights[i]
            # This item is too heavy so just take the best value we know from prev
            if item_weight > available_weight:
                dp[available_weight] = prev[available_weight]

            # Find what's better between 1.not taking the item or 2.taking it
            # 1.Best value we know about so far for the free space
            # 2.Subtract current item weight from available weight
            # Then add the current item value to the value we can carry with the newly subtracted weight
            else:
                dp[available_weight] = max(
                    prev[available_weight], values[i]+prev[available_weight-item_weight])

    return dp[-1]


@time_execution()
def knapsack_rec(values: list[int], weights: list[int], limit: int) -> int:
    if limit == 0:
        return 0
    if limit > sum(weights):
        return sum(values)

    def helper(idx: int, remaining_weight: int) -> int:
        if idx == len(values):
            return 0
        # Can't take item at index 'idx' because it's too heavy
        if weights[idx] > remaining_weight:
            return helper(idx+1, remaining_weight)

        # Max of taking the item and not taking the item
        return max(values[idx]+helper(idx+1, remaining_weight-weights[idx]), helper(idx+1, remaining_weight))

    return helper(0, limit)


@time_execution()
def knapsack_memo(values: list[int], weights: list[int], limit: int) -> int:
    if limit == 0:
        return 0
    if limit > sum(weights):
        return sum(values)

    memo = {}
    memo_hits = 0

    def helper(idx: int, remaining_weight: int) -> int:
        nonlocal memo_hits
        key = (idx, remaining_weight)

        if key in memo:
            memo_hits += 1
            return memo[key]
        if idx == len(values):
            return 0
        # Can't take item at index 'idx' because it's too heavy
        if weights[idx] > remaining_weight:
            return helper(idx+1, remaining_weight)

        # Max of taking the item and not taking the item
        memo[key] = max(values[idx]+helper(idx+1, remaining_weight -
                        weights[idx]), helper(idx+1, remaining_weight))
        return memo[key]

    return f"{helper(0, limit)}, memo hits: {memo_hits}"


values = [20, 30, 15, 25, 10, 20, 30, 15, 25, 10, 20, 30, 15, 25, 10]
weights = [50, 510, 5, 5, 5, 50, 510, 5, 5, 5, 50, 510, 5, 5, 5]
limit = 250

# values = [20, 30, 15, 25, 10]
# weights = [6, 13, 5, 10, 3]
# limit = 20

print(knapsack_dp(values, weights, limit))
print(knapsack_rec(values, weights, limit))
print(knapsack_memo(values, weights, limit))
