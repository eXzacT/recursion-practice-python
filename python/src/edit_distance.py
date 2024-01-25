'''What's the minimum number of insertions,deletions and substitutions to go from word1 to word2
    Also known as Levenshtein distance
'''
from common import time_execution
import networkx as nx


@time_execution()
def levenshtein_distance_dp(word1: str, word2: str) -> int:
    HEIGHT = len(word1)+1
    WIDTH = len(word2)+1
    dp = [[0]*WIDTH for _ in range(HEIGHT)]

    # Fill row and column with row/col index
    for i in range(1, HEIGHT):
        dp[i][0] = i
    for j in range(1, WIDTH):
        dp[0][j] = j

    for i in range(1, HEIGHT):
        for j in range(1, WIDTH):
            if word1[i-1] == word2[j-1]:  # Same characters, copy distance so far from topleft
                dp[i][j] = dp[i-1][j-1]
            else:  # Min distance so far between topleft, top and left positions +1
                dp[i][j] = 1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


@time_execution()
def levenshtein_distance_dp_v2(word1: str, word2: str) -> int:
    HEIGHT = len(word1)+1
    WIDTH = len(word2)+1

    # Fill row with its index value
    prev = []
    for j in range(WIDTH):
        prev.append(j)

    for i in range(1, HEIGHT):
        left = i  # First column in each row has the same value to the actual row index
        # Temporary list which has the updated values
        curr = [0]*WIDTH
        for j in range(1, WIDTH):
            if word1[i-1] == word2[j-1]:  # Same characters, copy distance from topleft
                curr[j] = prev[j-1]
            else:  # Best distance so far between topleft, top and left positions +1
                curr[j] = 1+min(prev[j-1], prev[j], left)
            # Number at the current position becomes left for the column in this row
            left = curr[j]

        # Make prev be the list with newly updated values, also change the first value to be same as row idx
        prev = curr
        prev[0] = i

    return prev[-1]


@time_execution()
def levenshtein_distance_rec(word1: str, word2: str) -> int:
    def helper(i: int, j: int) -> int:
        # What's the remaining length of a word we didn't fully traverse yet?
        if i == len(word1) or j == len(word2):
            # One of these will return 0 so it's as if it isn't there 0+x or x+0
            return len(word1)-i + len(word2)-j
        if word1[i] == word2[j]:
            return helper(i+1, j+1)

        # 3 choices, delete current letter from word1, add current letter from word2, replace
        # We don't actually have to do this, we can simulate it by increasing either or both indices
        return 1+min(helper(i+1, j), helper(i, j+1), helper(i+1, j+1))

    return helper(0, 0)


@time_execution(executions=100)
def levenshtein_distance_memo(word1: str, word2: str) -> int:
    memo = {}
    memo_hits = 0

    def helper(i: int, j: int) -> int:
        nonlocal memo_hits
        # What's the remaining length of a word we didn't fully traverse yet?
        if i == len(word1) or j == len(word2):
            return len(word1)-i + len(word2)-j
        key = (i, j)
        if key in memo:
            memo_hits += 1
            return memo[key]
        if word1[i] == word2[j]:
            memo[key] = helper(i+1, j+1)
            return memo[key]

        # 3 choices, delete current letter from word1, add current letter from word2, replace
        # We don't actually have to do this, we can simulate it by increasing either or both indices
        memo[key] = 1+min(helper(i+1, j), helper(i, j+1), helper(i+1, j+1))
        return memo[key]

    return f"{helper(0, 0)}, memo_hits: {memo_hits}"


@time_execution()
def levenshtein_distance_nx(word1: str, word2: str) -> int:
    G = nx.DiGraph()
    stack = [(0, 0)]
    visited = set()
    dummy_node = (-1, -1)

    while stack:
        i, j = stack.pop()
        if (i, j) in visited:
            continue
        visited.add((i, j))

        if i == len(word1) or j == len(word2):
            G.add_edge((i, j), dummy_node, weight=len(word1)-i + len(word2)-j)
            continue
        if word1[i] == word2[j]:
            G.add_edge((i, j), (i+1, j+1), weight=0)
            stack.append((i+1, j+1))
            continue

        G.add_edge((i, j), (i+1, j), weight=1)
        stack.append((i+1, j))
        G.add_edge((i, j), (i, j+1), weight=1)
        stack.append((i, j+1))
        G.add_edge((i, j), (i+1, j+1), weight=1)
        stack.append((i+1, j+1))

    return nx.shortest_path_length(G, source=(0, 0), target=dummy_node, weight="weight")


word1 = "inside"
word2 = "index"

print(levenshtein_distance_dp(word1, word2))
print(levenshtein_distance_dp_v2(word1, word2))
print(levenshtein_distance_rec(word1, word2))
print(levenshtein_distance_memo(word1, word2))
print(levenshtein_distance_nx(word1, word2))
