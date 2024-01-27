'''Given two strings s1 and s2, find the length of their shortest common supersequence'''

from longest_common_subsequence_len import lcs_len_dp, lcs_len_dp_v2, lcs_len_rec, lcs_len_memo, lcs_len_nx, lcs_len_hunt_szymanski
from common import time_execution
import networkx as nx


@time_execution()
def scs_dp(s1: str, s2: str) -> int:
    WIDTH = len(s2)+1
    HEIGHT = len(s1)+1
    dp = [[0]*WIDTH for _ in range(HEIGHT)]

    # When either strings are empty then their scs is the length of the other one
    for i in range(HEIGHT):
        dp[i][0] = i
    for j in range(WIDTH):
        dp[0][j] = j

    for i in range(1, HEIGHT):
        for j in range(1, WIDTH):
            if s1[i-1] == s2[j-1]:
                # Set current to be whatever was in topleft
                dp[i][j] = 1+dp[i-1][j-1]
            else:  # Set current to be 1+ minimum between above and left positions
                dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


@time_execution()
def scs_dp_v2(s1: str, s2: str) -> int:
    WIDTH = len(s2)+1
    HEIGHT = len(s1)+1

    prev = []
    for j in range(WIDTH):
        prev.append(j)

    for i in range(1, HEIGHT):
        left = i  # At the beginning of each outer loop set the left to be the actual index of the row
        temp = [0]*WIDTH
        for j in range(1, WIDTH):
            if s1[i-1] == s2[j-1]:
                # Set current to be whatever was in previous row but 1 pos left
                temp[j] = 1+prev[j-1]
            else:  # Set current to be 1+ minimum between same col in prev row and the number on the left
                temp[j] = 1+min(prev[j], left)

            # Update left to be what the current is
            left = temp[j]

        # Update prev to be the newly updated row and set its 0th element to be same as row index
        prev = temp
        prev[0] = i

    return prev[-1]


@time_execution()
def scs_rec(s1: str, s2: str) -> int:
    def helper(i: int, j: int) -> int:
        # Return the remaining length of whichever string we didn't fully traverse yet
        if i == len(s1) or j == len(s2):
            return len(s1)-i + len(s2)-j

        if s1[i] == s2[j]:
            return 1+helper(i+1, j+1)
        return 1+min(helper(i+1, j), helper(i, j+1))

    return helper(0, 0)


@time_execution()
def scs_memo(s1: str, s2: str) -> int:
    memo = {}
    memo_hits = 0

    def helper(i: int, j: int) -> int:
        nonlocal memo_hits
        key = (i, j)
        # Return the remaining length of whichever string we didn't fully traverse yet
        if i == len(s1) or j == len(s2):
            return len(s1)-i + len(s2)-j
        if key in memo:
            memo_hits += 1
            return memo[key]

        if s1[i] == s2[j]:
            memo[key] = 1+helper(i+1, j+1)
            return memo[key]

        memo[key] = 1+min(helper(i+1, j), helper(i, j+1))
        return memo[key]

    return f"{helper(0, 0)}, memo_hits: {memo_hits}"


@time_execution()
def scs_nx(s1: str, s2: str) -> int:
    G = nx.DiGraph()
    stack = [(0, 0)]
    visited = set()
    dummy_node = (-1, -1)

    while stack:
        i, j = stack.pop()
        if (i, j) in visited:
            continue
        visited.add((i, j))

        if i == len(s1) or j == len(s2):
            G.add_edge((i, j), dummy_node, weight=len(s1)-i + len(s2)-j)
            continue
        if s1[i] == s2[j]:
            G.add_edge((i, j), (i+1, j+1), weight=1)
            stack.append((i+1, j+1))
        else:
            G.add_edge((i, j), (i+1, j), weight=1)
            stack.append((i+1, j))
            G.add_edge((i, j), (i, j+1), weight=1)
            stack.append((i, j+1))

    return nx.shortest_path_length(G, source=(0, 0), target=dummy_node, weight="weight")


s1 = "abdacbab"
s2 = "acebfca"

# Note, this can also be calculated with len(s1)+len(s2)-LCS(s1,s2) formula
# So add their lengths and subtract length of their shortest common subsequence
print(scs_dp(s1, s2))
print(len(s1)+len(s2)-lcs_len_dp(s1, s2))

print(scs_dp_v2(s1, s2))
print(len(s1)+len(s2)-lcs_len_dp_v2(s1, s2))

print(scs_rec(s1, s2))
print(len(s1)+len(s2)-lcs_len_rec(s1, s2))

print(scs_memo(s1, s2))
print(len(s1)+len(s2)-lcs_len_memo(s1, s2))

print(scs_nx(s1, s2))
print(len(s1)+len(s2)-lcs_len_nx(s1, s2))

print(len(s1)+len(s2)-lcs_len_hunt_szymanski(s1, s2))
