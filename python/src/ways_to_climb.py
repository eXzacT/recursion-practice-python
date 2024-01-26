'''Given stairs of length 'n', and a set of possible ways to jump,
    What are all the ways we can climb to the top of those stairs?(permutations allowed)
'''

from common import time_execution
import networkx as nx


@time_execution()
def ways_to_climb_dp(n: int, jumps: list[int]) -> int:
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(n+1):
        if dp[i]:  # We can skip if this step is 0
            for jump in jumps:
                if (ni := i+jump) <= n:
                    # To get to i+jump we can use all the ways we got to i
                    dp[ni] += dp[i]

    return dp[-1]


@time_execution()
def ways_to_climb_rec(n: int, jumps: list[int]) -> int:
    def helper(remainder: int) -> int:
        if remainder == 0:
            return 1

        count = 0
        for jump in jumps:
            if remainder-jump >= 0:
                count += helper(remainder-jump)

        return count

    return helper(n)


@time_execution()
def ways_to_climb_memo(n: int, jumps: list[int]) -> int:
    memo = {0: 1}
    memo_hits = 0

    def helper(remainder: int) -> int:
        nonlocal memo_hits

        if remainder in memo:
            memo_hits += 1
            return memo[remainder]

        count = 0
        for jump in jumps:
            if remainder-jump >= 0:
                count += helper(remainder-jump)

        memo[remainder] = count
        return count

    return f"{helper(n)}, memo_hits: {memo_hits}"


@time_execution()
def ways_to_climb_nx(n: int, jumps: list[int]) -> int:
    def helper(remainder: int) -> None:
        if remainder == 0:
            return

        for jump in jumps:
            if remainder-jump >= 0:
                G.add_edge(remainder, remainder-jump)
                helper(remainder-jump)

    G = nx.DiGraph()
    helper(n)

    return len(list(nx.all_simple_paths(G, source=n, target=0)))


print(ways_to_climb_dp(10, [2, 4, 5, 8]))
print(ways_to_climb_rec(10, [2, 4, 5, 8]))
print(ways_to_climb_memo(10, [2, 4, 5, 8]))
print(ways_to_climb_nx(10, [2, 4, 5, 8]))
