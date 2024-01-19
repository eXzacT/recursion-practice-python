'''Given a 2d matrix, find the min cost path from top right to bottom left
    You can only go down and right
'''
from common import time_execution
from collections import deque
import heapq
import networkx as nx


@time_execution()
def min_cost_path_dp(grid: list[list[int]]) -> int:
    HEIGHT, WIDTH = len(grid), len(grid[0])
    dp = [[0]*WIDTH for _ in range(HEIGHT)]
    dp[0][0] = grid[0][0]

    # Fill out the first row, example [3,6,9,12]-->[3,9,18,30]
    for j in range(1, WIDTH):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    # Fill out the first column
    for i in range(1, HEIGHT):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill up the rest of the DP table
    for i in range(1, HEIGHT):
        for j in range(1, WIDTH):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


@time_execution()
def min_cost_path_rec(grid: list[list[int]]) -> list[int]:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)

    def helper(m: int, n: int):
        if m == HEIGHT-1 and n == WIDTH-1:
            return grid[m][n]
        if m == HEIGHT-1:  # Can only go right
            return grid[m][n]+helper(m, n+1)
        if n == WIDTH-1:  # Can only go left
            return grid[m][n]+helper(m+1, n)

        return grid[m][n]+min(helper(m+1, n), helper(m, n+1))

    return helper(0, 0)


@time_execution()
def min_cost_path_memo(grid: list[list[int]]) -> list[int]:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)
    memo = {(HEIGHT-1, WIDTH-1): grid[-1][-1]}
    memo_hits = 0

    def helper(m: int, n: int):
        key = (m, n)
        nonlocal memo_hits

        if key in memo:
            memo_hits += 1
            return memo[key]
        if m == HEIGHT-1:  # Can only go right
            return grid[m][n]+helper(m, n+1)
        if n == WIDTH-1:  # Can only go left
            return grid[m][n]+helper(m+1, n)

        memo[key] = grid[m][n]+min(helper(m+1, n), helper(m, n+1))
        return memo[key]

    return f"{helper(0, 0)}, memo hits: {memo_hits}"


@time_execution()
def min_cost_path_nx(grid: list[list[int]]) -> list[int]:
    G = nx.DiGraph()
    WIDTH = len(grid[0])
    HEIGHT = len(grid)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if j < WIDTH - 1:  # If not on the last column, add edge to the right
                G.add_edge((i, j), (i, j + 1), weight=grid[i][j])
            if i < HEIGHT - 1:  # If not on the last row, add edge below
                G.add_edge((i, j), (i + 1, j), weight=grid[i][j])

    # Have to add the end node value itself
    return nx.shortest_path_length(G, source=(0, 0), target=(HEIGHT - 1, WIDTH - 1), weight='weight') + grid[HEIGHT - 1][WIDTH - 1]


@time_execution()
def min_cost_path_bfs(grid: list[list[int]]) -> list[int]:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)
    min_dist = float('inf')

    minheap = deque([(0, 0, 0)])
    while minheap:
        row, col, dist = minheap.popleft()
        if 0 <= row < HEIGHT and 0 <= col < WIDTH:
            dist += grid[row][col]
            # Did we reach the end?
            if (row, col) == (HEIGHT-1, WIDTH-1):
                min_dist = min(dist, min_dist)
            # Can only go down and right
            for nx, ny in [(row, col+1), (row+1, col)]:
                minheap.append((nx, ny, dist))

    return min_dist


@time_execution()
def min_cost_path_dijkstra(grid: list[list[int]]) -> list[int]:
    WIDTH = len(grid[0])
    HEIGHT = len(grid)
    tie_breaker = 0

    # Dist, tie_breaker, row,col
    minheap = [(0, tie_breaker, 0, 0)]
    while minheap:
        dist, _, row, col = heapq.heappop(minheap)
        if 0 <= row < HEIGHT and 0 <= col < WIDTH:
            dist += grid[row][col]
            # With dijkstra we can guarantee this is shortest path so just return
            if (row, col) == (HEIGHT-1, WIDTH-1):
                return dist
            # Can only go down and right
            for nx, ny in [(row, col+1), (row+1, col)]:
                heapq.heappush(
                    minheap, (dist, (tie_breaker := tie_breaker+1), nx, ny))


matrix = [[3, 2, 12, 15, 10],
          [6, 19, 7, 11, 17],
          [8, 5, 12, 32, 21],
          [3, 20, 2, 9, 7]]

print(min_cost_path_dp(matrix))
print(min_cost_path_rec(matrix))
print(min_cost_path_memo(matrix))
print(min_cost_path_nx(matrix))
print(min_cost_path_bfs(matrix))
print(min_cost_path_dijkstra(matrix))
