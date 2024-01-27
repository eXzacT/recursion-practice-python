# Print all longest common sub-sequences in lexicographical order
from common import time_execution


@time_execution()
def increasing_lcs_rec(s1: str, s2: str) -> list[str]:
    sub_sequences = []

    def helper(s1: str, start=0, string_so_far=''):
        # Reached the end of either strings
        # Using indexes for second one to optimize
        if s1 == '' or start == len(s2):
            sub_sequences.append(string_so_far)
        for idx in range(start, len(s2)):
            char = s2[idx]
            if char not in s1:
                continue
            # Passing a slice from where the character was found not incl
            helper(s1[s1.find(char)+1:], idx+1, string_so_far+char)

    helper(s1)
    return sorted(list(filter(lambda x: len(x) == len(max(sub_sequences, key=len)), sub_sequences)))


@time_execution()
def increasing_lcs_memo(s1: str, s2: str) -> list:

    sub_sequences = []
    memo_hit = 0
    memo = {}

    def helper(s1: str, start=0, string_so_far=''):
        # Not sure why it's faster for s1 instead of start for key but has less hits
        nonlocal memo_hit
        key = (s1, string_so_far)
        if s1 == '' or start == len(s2):
            sub_sequences.append(string_so_far)
            return
        if key in memo:
            memo_hit += 1
            return memo[key]
        for idx in range(start, len(s2)):
            char = s2[idx]
            if char not in s1:
                continue

            helper(s1[s1.find(char)+1:], idx+1, string_so_far+char)

        memo[key] = sub_sequences
        return memo[key]

    helper(s1)
    return sorted(list(filter(lambda x: len(x) == len(max(sub_sequences, key=len)), sub_sequences))), f"Memo hits: {memo_hit}"


@time_execution()
def increasing_lcs_dp(s1: str, s2: str) -> list[str]:
    m, n = len(s1), len(s2)
    dp = [[set() for _ in range(n+1)] for __ in range(m+1)]
    # The LCS of an empty string and any other string is an empty string
    for i in range(m+1):
        dp[i][0] = {""}
    for j in range(n+1):
        dp[0][j] = {""}

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                # Add current character to each substring positioned [i-1][j-1]
                dp[i][j] = {lcs + s1[i-1] for lcs in dp[i-1][j-1]}
            else:  # Copyover longer substring from pos [i-1][j] or [i][j-1]
                if len(max(dp[i-1][j], key=len)) > len(max(dp[i][j-1], key=len)):
                    dp[i][j] = dp[i-1][j]
                elif len(max(dp[i-1][j], key=len)) < len(max(dp[i][j-1], key=len)):
                    dp[i][j] = dp[i][j-1]
                else:  # If they're same length then do a union
                    dp[i][j] = dp[i-1][j] | dp[i][j-1]

    # The bottom-right cell contains all LCSs of s1 and s2
    return sorted(dp[m][n])


s1 = 'ABCBDABABCBDAB'
s2 = 'BDCABBDCAB'
print(increasing_lcs_dp(s1, s2))
print(increasing_lcs_rec(s1, s2))
print(increasing_lcs_memo(s1, s2))
