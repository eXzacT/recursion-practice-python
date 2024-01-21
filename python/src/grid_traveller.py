'''Given an m*n grid how many ways can you get from top left to bottom right
    You can only go down or right
'''
from common import time_execution


@time_execution()
def grid_traveller_tabulation(m: int, n: int) -> int:
    dp = [[0 for _ in range(n)]for _ in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            current = dp[i][j]
            if i+1 < m:
                dp[i+1][j] += current
            if j+1 < n:
                dp[i][j+1] += current

    return dp[-1][-1]


@time_execution(executions=100)
def grid_traveller_tabulation_v2(m: int, n: int) -> int:
    dp = [[0 for _ in range(n)]for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1

    for j in range(1, n):
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]

    return dp[-1][-1]


@time_execution(executions=100)
def grid_traveller_tabulation_v3(m: int, n: int) -> int:
    dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]

    return dp[-1][-1]


@time_execution()
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


@time_execution()
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


@time_execution()
def grid_traveller_rec_v2(m: int, n: int) -> int:
    def helper(m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        return helper(m-1, n) + helper(m, n-1)

    return helper(m, n)


@time_execution()
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


@time_execution()
def grid_traveller_rec_v3(m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0

    def helper(m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        down = right = 0
        if m > 1:
            down = helper(m-1, n)
        if n > 1:
            right = helper(m, n-1)

        return down+right

    return helper(m, n)


print(grid_traveller_tabulation(10, 10))
print(grid_traveller_tabulation_v2(10, 10))
print(grid_traveller_tabulation_v3(10, 10))
print(grid_traveller_rec(10, 10))
print(grid_traveller_rec_v3(10, 10))
print(grid_traveller_rec_memo(10, 10))
print(grid_traveller_rec_v2(10, 10))
print(grid_traveller_rec_v2_memo(10, 10))
