'''Given a grid where 1 represents a wall and 0 represents a path you can go over
    how many ways can you get from top left to bottom right
'''
from common import time_execution


@time_execution()
def paths_dp(grid: list[list[int]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)
    dp = [[0]*WIDTH for _ in range(HEIGHT)]
    dp[0][0] = 1

    # Fill the column, as soon as we reach a wall stop since we can't reach the positions after it
    for i in range(HEIGHT):
        if grid[i][0]:  # 1 is truthy==wall
            break
        dp[i][0] = 1

    # Fill the row, as soon as we reach a wall stop since we can't reach the positions after it
    for j in range(WIDTH):
        if grid[0][j]:  # 1 is truthy==wall
            break
        dp[0][j] = 1

    for i in range(1, HEIGHT):
        for j in range(1, WIDTH):
            # Do not update this position if it's a wall
            if grid[i][j]:
                continue
            # Sum of ways to get to the above and left position are ways to get to this position
            dp[i][j] = dp[i-1][j]+dp[i][j-1]

    return dp[-1][-1]


@time_execution()
def paths_rec(grid: list[list[int]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)

    def helper(x: int, y: int) -> int:
        # Out of bounds or hit a wall
        if x == WIDTH or y == HEIGHT or grid[y][x]:
            return 0
        if x == WIDTH-1 and y == HEIGHT-1:  # Got to the end position
            return 1

        down = right = 0
        if 0 <= x < HEIGHT:
            down = helper(x+1, y)
        if 0 <= y < WIDTH:
            right = helper(x, y+1)

        return down+right

    return helper(0, 0)


@time_execution()
def paths_memo(grid: list[list[int]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)
    memo = {(WIDTH-1, HEIGHT-1): 1}
    memo_hits = 0

    def helper(x: int, y: int) -> int:
        # Out of bounds or hit a wall
        nonlocal memo_hits
        key = (x, y)

        if x == WIDTH or y == HEIGHT or grid[y][x]:
            return 0
        if key in memo:
            memo_hits += 1
            return memo[key]

        down = right = 0
        if 0 <= x < HEIGHT:
            down = helper(x+1, y)
        if 0 <= y < WIDTH:
            right = helper(x, y+1)

        memo[key] = down+right
        return memo[key]

    return f"{helper(0, 0)}, memo hits: {memo_hits}"


grid = [[0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0]]

print(paths_dp(grid))
print(paths_rec(grid))
print(paths_memo(grid))
