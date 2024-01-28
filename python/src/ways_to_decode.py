'''Given an encoded string s made of numbers, find the number of possible ways to decode it
    A string made of letters can be encoded by replacing each letter by its position in the alphabet 
    but when decoding, a same encoded string can have multiple ways to be decoded 
    (e.g.: 5124 can be decoded as 5 1 2 4 (EABD), or 5 12 4 (ELD), or 5 1 24 (EAX)).
'''
from common import time_execution
import networkx as nx


def ways_to_decode_dp(s: str) -> int:
    dp = [0]*len(s)

    # Edge cases
    if s[0] == '0':
        return 0
    if len(s) == 1:
        return 1

    # At position 0 we only have 1 possible way to decode, because only 1 number
    dp[0] = 1
    # If the digit is 10 or 20 then it's still only 1 way to decode because later we would have a 0 by itself
    # If the digit is not 10 or 20 and it's between 10 and 26(incl) then we can have 2 ways to decode
    dp[1] = (s[1] != "0") + (10 <= int(s[0]+s[1]) <= 26)

    for i in range(2, len(s)):
        # If current digit is not a 0 we could have gotten here from prev pos
        if s[i] != '0':
            dp[i] += dp[i-1]
        # We also could have gotten here if the previous digit and this digit together are between 10-26
        # Meaning we jumped from i-2th position
        if 10 <= int(s[i-1]+s[i]) <= 26:
            dp[i] += dp[i-2]

    print(dp)
    return dp[-1]


@time_execution()
def ways_to_decode_rec(s: str) -> int:
    def helper(i: int):
        # -1 because we're accessing s[i+1] later in the code
        if i >= len(s)-1:
            return 1
        # Failed path because there is no 0th alphabet element(not 0 based indexing)
        if s[i] == '0':
            return 0

        # If we can add 2 digits together and still get the alphabet index
        if 10 <= int(s[i]+s[i+1]) <= 26:
            return helper(i+2)+helper(i+1)

        return helper(i+1)

    return helper(0)


@time_execution()
def ways_to_decode_memo(s: str) -> int:
    memo = {}
    memo_count = 0

    def helper(i: int):
        nonlocal memo_count
        # -1 because we're accessing s[i+1] later in the code
        if i >= len(s)-1:
            return 1
        if s[i] == '0':
            return 0
        if i in memo:
            memo_count += 1
            return memo[i]

        # If we can add 2 digits together and still get the alphabet index
        if 10 <= int(s[i]+s[i+1]) <= 26:
            memo[i] = helper(i+2)+helper(i+1)
            return memo[i]

        memo[i] = helper(i+1)
        return memo[i]

    return f"{helper(0)}, memo_count: {memo_count}"


@time_execution()
def ways_to_decode_nx(s: str) -> int:
    def helper(i: int) -> None:
        if i == len(s)-1:
            return
        if s[i] == '0':  # Stop drawing edges
            return

        if 10 <= int(s[i]+s[i+1]) <= 26:
            G.add_edge(i, i+1)
            helper(i+1)
            G.add_edge(i, i+2)
            helper(i+2)
        else:
            G.add_edge(i, i+1)
            helper(i+1)

    G = nx.DiGraph()
    helper(0)

    # How many paths are there from index 0 to len-1
    return len(list(nx.all_simple_paths(G, source=0, target=len(s)-1)))


print(ways_to_decode_dp("512810120129"))
print(ways_to_decode_rec("512810120129"))
print(ways_to_decode_memo("512810120129"))
print(ways_to_decode_nx("512810120129"))
