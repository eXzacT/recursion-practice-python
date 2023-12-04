# Traveller on a 2d grid, how many ways can you travel
# from top left to bottom right, can only move down or right
from common import time_execution


@time_execution
def grid_traveller_tabulation(m: int, n: int) -> int:
    table = [[0 for _ in range(n+1)]for _ in range(m+1)]
    table[0][0] = 1

    for i in range(m):
        for j in range(n):
            current = table[i][j]
            if i+1 < m:
                table[i+1][j] += current
            if j+1 < n:
                table[i][j+1] += current

    return table[i][j]


@time_execution
def grid_traveller_rec(m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0

    def helper(start_m: int, start_n: int) -> int:
        if start_m == m and start_n == n:
            return 1
        if start_m == m:
            return helper(start_m, start_n+1)
        if start_n == n:
            return helper(start_m+1, start_n)
        return helper(start_m+1, start_n) + helper(start_m, start_n+1)

    return helper(1, 1)


@time_execution
def grid_traveller_rec_memo(m: int, n: int) -> int:
    # Invalid grid
    if m == 0 or n == 0:
        return 0
    memo = {(m, n): 1}

    # Debug
    memo_usages = 0
    recursive_calls = 0

    def helper(start_m: int, start_n: int) -> int:
        # Debug
        nonlocal memo_usages
        nonlocal recursive_calls
        recursive_calls += 1

        key = (start_m, start_n)
        reversed_key = (start_n, start_m)

        if key in memo or reversed_key in memo:
            memo_usages += 1
            return memo[key]
        if start_m == m:
            return helper(start_m, start_n+1)
        if start_n == n:
            return helper(start_m+1, start_n)

        memo[key] = helper(start_m+1, start_n) + helper(start_m, start_n+1)
        memo[reversed_key] = memo[key]
        return memo[key]

    return f"Result is: {helper(1, 1)}\nMemo calls: {memo_usages}\nRecursive calls:{recursive_calls}"


@time_execution
def grid_traveller_rec_v2(m: int, n: int) -> int:
    def helper(m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        return helper(m-1, n) + helper(m, n-1)

    return helper(m, n)


@time_execution
def grid_traveller_rec_v2_memo(m: int, n: int) -> int:
    memo = {(1, 1): 1}

    # Debug
    memo_usages = 0
    recursive_calls = 0

    def helper(m: int, n: int) -> int:
        # Debug
        nonlocal memo_usages
        nonlocal recursive_calls
        recursive_calls += 1

        key = (m, n)
        reversed_key = (n, m)

        if key in memo or reversed_key in memo:
            memo_usages += 1
            return memo[key]
        if m == 0 or n == 0:
            return 0

        memo[key] = memo[reversed_key] = helper(m-1, n) + helper(m, n-1)

        return memo[key]

    return f"Result is: {helper(m, n)}\nMemo calls: {memo_usages}\nRecursive calls:{recursive_calls}"


print(grid_traveller_tabulation(10, 10))
print(grid_traveller_rec(10, 10))
print(grid_traveller_rec_memo(10, 10))
print(grid_traveller_rec_v2(10, 10))
print(grid_traveller_rec_v2_memo(10, 10))
