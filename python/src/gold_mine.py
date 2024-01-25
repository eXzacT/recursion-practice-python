'''Given a grid of m*n positions, where each value in the grid represents how much gold there is at that pos
    What's the greatest amount of gold you can dig by starting from any positions in first row
    and exiting at any position in the bottom row?
    We are only allowed to dig down, downleft and downright
'''
from common import time_execution
import networkx as nx


@time_execution()
def gold_mine_iter(grid: list[list[int]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)
    grid = {complex(i, j): val for i, row in enumerate(grid)
            for j, val in enumerate(row)}

    # Start from every possible position in the first row Start from every possible position in the first row
    stack = [(complex(0, j), 0) for j in range(WIDTH)]
    max_val = 0
    while stack:
        pos, val = stack.pop()
        if pos in grid:
            val += grid[pos]
            if pos.real == HEIGHT-1:  # Reached the row and can't keep traversing update max if it's max
                max_val = max(max_val, val)
                continue
            # Go down,downleft, downright
            for npos in [pos+1, pos+1+1j, pos+1-1j]:
                stack.append((npos, val))

    return max_val


@time_execution()
def gold_mine_dp(grid: list[list[int]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)
    dp = grid[0].copy()
    # Keep updating by max value between the 3 adjacent neighbours under each current position
    for i in range(1, HEIGHT):
        temp = dp.copy()  # So we don't overwrite the current row values when updating
        for j in range(WIDTH):
            if j == 0:  # Only middle and right because we're at the start
                dp[j] = max(temp[j], temp[j+1])+grid[i][j]
            elif j == WIDTH-1:  # Only middle and left because we're at the end
                dp[j] = max(temp[j-1], temp[j])+grid[i][j]
            else:  # Left, middle, right
                dp[j] = max(temp[j-1], temp[j], temp[j+1])+grid[i][j]

    return max(dp)


@time_execution()
def gold_mine_rec(grid: list[list[int]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)

    def helper(i: int, j: int) -> int:
        if j < 0 or j == WIDTH:
            return 0
        if i == HEIGHT-1:  # Reached last row
            return grid[i][j]

        # Max for digging down,downleft and downright
        max_val = max(helper(i+1, j), helper(i+1, j-1), helper(i+1, j+1))
        return grid[i][j]+max_val

    # Max value starting from each position in first row
    return max([helper(0, j) for j in range(WIDTH)])


@time_execution()
def gold_mine_memo(grid: list[list[int]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)
    memo = {}
    memo_hits = 0

    def helper(i: int, j: int) -> int:
        key = (i, j)
        nonlocal memo_hits
        if key in memo:
            memo_hits += 1
            return memo[key]
        if j < 0 or j == WIDTH:
            return 0
        if i == HEIGHT-1:  # Reached last row
            return grid[i][j]

        # Max for digging down,downleft and downright
        memo[key] = max(helper(i+1, j), helper(i+1, j-1),
                        helper(i+1, j+1))+grid[i][j]
        return memo[key]

    # Max value starting from each position in first row
    return f"{max([helper(0, j) for j in range(WIDTH)])}, memo_hits:{memo_hits}"


@time_execution()
def gold_mine_nx(grid: list[list[int]]) -> int:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)
    G = nx.DiGraph()
    # Node we use to connect to each of the nodes in the first row, because we want to add their weight too
    dummy_node = (-1, -1)

    for i in range(HEIGHT-1):
        for j in range(WIDTH):
            if i == 0:  # Without this the longest path wouldn't add the start node value to the weight
                G.add_edge(dummy_node, (i, j), weight=grid[i][j])
            if j != 0:  # If it's not the beginning of the row we can add the downleft since it's in bounds
                G.add_edge((i, j), (i+1, j-1), weight=grid[i+1][j-1])
            if j != WIDTH-1:  # If it's not the end of the row we can add the downright since it's in bounds
                G.add_edge((i, j), (i+1, j+1), weight=grid[i+1][j+1])
            G.add_edge((i, j), (i+1, j), weight=grid[i+1][j])

    return nx.dag_longest_path_length(G, weight='weight')


mine = [
    [3, 2, 12, 15, 10],
    [6, 19, 7, 11, 17],
    [8, 5, 12, 32, 21],
    [3, 20, 2, 9, 7],
]

print(gold_mine_dp(mine))
print(gold_mine_iter(mine))
print(gold_mine_rec(mine))
print(gold_mine_memo(mine))
print(gold_mine_nx(mine))
