'''Find the length of longest common sequence of two strings
    example "abdacbab" and "acebfca", abca is in both those strings(not necessarily right after the other)
'''
import bisect
import networkx as nx
from common import time_execution
from collections import defaultdict


@time_execution()
def lcs_len_dp(s1: str, s2: str) -> int:
    WIDTH = len(s2)+1
    HEIGHT = len(s1)+1
    dp = [[0]*WIDTH for _ in range(HEIGHT)]
    for i in range(1, HEIGHT):
        for j in range(1, WIDTH):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


@time_execution()
def lcs_len_dp_v2(s1: str, s2: str) -> int:
    WIDTH = len(s2)+1
    HEIGHT = len(s1)+1

    prev = [0]*WIDTH

    for i in range(1, HEIGHT):
        left = 0
        for j in range(1, WIDTH):
            if s1[i-1] == s2[j-1]:
                prev[j] = 1+left
            else:
                prev[j] = max(prev[j], left)

            left = prev[j]

    return prev[-1]


@time_execution()
def lcs_len_hunt_szymanski(a: str, b: str) -> int:
    a_indices = defaultdict(list)

    # Create a dictionary of chars and its positions
    for idx, char in enumerate(a):
        a_indices[char].append(idx)

    # Then reverse those positions for each char
    for idx in a_indices.values():
        idx.reverse()

    a_filtered = []
    # Create a list of indices in str1 for each character in str2 that is also in str1
    # This list is created in the order of characters in str2
    for char in b:
        a_filtered.extend(a_indices[char])

    lcs = []
    for ai in a_filtered:
        # Find the position to insert the current index in the LCS list to keep it sorted
        pos = bisect.bisect_left(lcs, ai)
        # If the position is at the end of the LCS list, we can just append it
        # Otherwise, replace the element at found position with current index
        if pos == len(lcs):
            lcs.append(ai)
        else:
            lcs[pos] = ai

    return len(lcs)


@time_execution()
def lcs_len_rec(s1: str, s2: str) -> int:
    def helper(i: int, j: int) -> int:
        if i == len(s1) or j == len(s2):
            return 0

        if s1[i] == s2[j]:
            return 1+helper(i+1, j+1)

        return max(helper(i+1, j), helper(i, j+1))

    return helper(0, 0)


@time_execution()
def lcs_len_memo(s1: str, s2: str) -> int:
    memo = {}
    memo_hits = 0

    def helper(i: int, j: int) -> int:
        nonlocal memo_hits
        key = (i, j)

        if key in memo:
            memo_hits += 1
            return memo[key]

        if i == len(s1) or j == len(s2):
            return 0

        if s1[i] == s2[j]:
            memo[key] = 1+helper(i+1, j+1)
            return memo[key]

        memo[key] = max(helper(i+1, j), helper(i, j+1))
        return memo[key]

    return helper(0, 0)
    # return f"{helper(0, 0)}, memo_hits: {memo_hits}"


@time_execution()
def lcs_len_nx(s1: str, s2: str) -> int:
    G = nx.DiGraph()
    stack = [(0, 0)]
    visited = set()

    while stack:
        i, j = stack.pop()
        if (i, j) in visited:
            continue
        visited.add((i, j))

        if i == len(s1) or j == len(s2):
            continue
        if s1[i] == s2[j]:
            G.add_edge((i, j), (i+1, j+1), weight=1)
            stack.append((i+1, j+1))
            continue
        else:
            G.add_edge((i, j), (i+1, j), weight=0)
            stack.append((i+1, j))
            G.add_edge((i, j), (i, j+1), weight=0)
            stack.append((i, j+1))

    return nx.dag_longest_path_length(G)


if __name__ == "__main__":
    s1 = "abracadabraalakazam"
    s2 = "aceofspadesjackofhearts"

    print(lcs_len_dp(s1, s2))
    print(lcs_len_dp_v2(s1, s2))
    print(lcs_len_hunt_szymanski(s1, s2))
    # print(lcs_len_rec(s1, s2))
    print(lcs_len_memo(s1, s2))
    print(lcs_len_nx(s1, s2))
