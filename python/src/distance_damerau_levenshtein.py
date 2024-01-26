'''What's the minimum number of insertions, deletions, substitutions or the transposition of two adjacent characters
    to make word1 and word2 equal, also known as Damerau-Levenshtein distance
'''
from common import time_execution


@time_execution()
def damerau_levenshtein_dp(word1: str, word2: str) -> int:
    WIDTH = len(word2)+1
    HEIGHT = len(word1)+1
    dp = [[0]*WIDTH for _ in range(HEIGHT)]

    # Fill first row and first column with their index
    for i in range(1, HEIGHT):
        dp[i][0] = i
    for j in range(1, WIDTH):
        dp[0][j] = j

    for i in range(1, HEIGHT):
        for j in range(1, WIDTH):
            # Characters are the same, copy value from topleft
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # We can swap them, but we already counted +1 before so just copy this time(swap=1 operation)
            elif i < HEIGHT-1 and j < WIDTH-1 and word1[i-1] == word2[j] and word1[i] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Min between topleft, top and left
                dp[i][j] = 1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


@time_execution()
def damerau_levenshtein_dp_v2(word1: str, word2: str) -> int:
    WIDTH = len(word2)+1
    HEIGHT = len(word1)+1

    # Fill row with its index value
    prev = []
    for j in range(WIDTH):
        prev.append(j)

    for i in range(1, HEIGHT):
        left = i
        curr = [0]*WIDTH
        for j in range(1, WIDTH):
            if word1[i-1] == word2[j-1]:
                curr[j] = prev[j-1]
            elif i < HEIGHT-1 and j < WIDTH-1 and word1[i] == word2[j-1] and word1[i-1] == word2[j]:
                curr[j] = prev[j-1]
            else:  # Best distance so far between topleft, top and left positions +1
                curr[j] = 1+min(prev[j-1], prev[j], left)
            # Update left to be the current element
            left = prev[j]

        # Make prev be the list with newly updated values, also change the first value to be same as row idx
        prev = curr
        prev[0] = i

    return prev[-1]


@time_execution()
def damerau_levenshtein_rec(word1: str, word2: str) -> int:
    def helper(i: int, j: int) -> int:
        # Get the remaining length of whichever word we didn't traverse yet
        if i == len(word1) or j == len(word2):
            return len(word1)-i + len(word2)-j

        # Check next letter for each word
        if word1[i] == word2[j]:
            return helper(i+1, j+1)

        res = 1+min(helper(i + 1, j),    # deletion
                    helper(i, j + 1),    # insertion
                    helper(i + 1, j + 1))  # substitution

        # Can we swap characters at i and j+1 or j and i+1 to make them the same?
        if (i + 1 < len(word1) and j + 1 < len(word2) and
                word1[i] == word2[j + 1] and word1[i + 1] == word2[j]):
            # If we can then we only did 1 operation, also skip to +2 since we made current and +1 equal
            res = min(res, 1+helper(i + 2, j + 2))

        return res

    return helper(0, 0)


@time_execution()
def damerau_levenshtein_memo(word1: str, word2: str) -> int:
    memo = {}
    memo_hits = 0

    def helper(i: int, j: int) -> int:
        nonlocal memo_hits
        key = (i, j)

        # Get the remaining length of whichever word we didn't traverse yet
        if i == len(word1) or j == len(word2):
            return len(word1)-i + len(word2)-j
        if key in memo:
            memo_hits += 1
            return memo[key]

        # Check next letter for each word
        if word1[i] == word2[j]:
            memo[key] = helper(i+1, j+1)
            return memo[key]

        res = 1+min(helper(i + 1, j),    # deletion
                    helper(i, j + 1),    # insertion
                    helper(i + 1, j + 1))  # substitution

        # Can we swap characters at i and j+1 or j and i+1 to make them the same?
        if (i + 1 < len(word1) and j + 1 < len(word2) and
                word1[i] == word2[j + 1] and word1[i + 1] == word2[j]):
            # If we can then we only did 1 operation, also skip to +2 since we made current and +1 equal
            res = min(res, 1+helper(i + 2, j + 2))

        memo[key] = res
        return res

    return f"{helper(0, 0)}, memo_hits: {memo_hits}"


word1 = "aether"
word2 = "eat"

print(damerau_levenshtein_dp(word1, word2))
print(damerau_levenshtein_dp_v2(word1, word2))
print(damerau_levenshtein_rec(word1, word2))
print(damerau_levenshtein_memo(word1, word2))
