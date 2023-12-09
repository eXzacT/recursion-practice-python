# Print all longest common sub-sequences in lexicographical order
from pprint import pprint
from common import time_execution

# TODO memoize this


@time_execution()
def longest_common_sub_sequences_rec(s1: str, s2: str) -> list[str]:
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
def longest_common_sub_sequences_tabulation(s1: str, s2: str) -> list[str]:
    m, n = len(s1), len(s2)
    table = [[set() for _ in range(n+1)] for __ in range(m+1)]
    # The LCS of an empty string and any other string is an empty string
    for i in range(m+1):
        table[i][0] = {""}
    for j in range(n+1):
        table[0][j] = {""}

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                # Add current character to each substring positioned [i-1][j-1]
                table[i][j] = {lcs + s1[i-1] for lcs in table[i-1][j-1]}
            else:  # Copyover longer substring from pos [i-1][j] or [i][j-1]
                if len(max(table[i-1][j], key=len)) > len(max(table[i][j-1], key=len)):
                    table[i][j] = table[i-1][j]
                elif len(max(table[i-1][j], key=len)) < len(max(table[i][j-1], key=len)):
                    table[i][j] = table[i][j-1]
                else:  # If they're same length then do a union
                    table[i][j] = table[i-1][j] | table[i][j-1]

    # pprint(table)
    # The bottom-right cell contains all LCSs of s1 and s2
    return sorted(table[m][n])


print(longest_common_sub_sequences_tabulation('ABCBDAB', 'BDCAB'))
print(longest_common_sub_sequences_rec('ABCBDAB', 'BDCAB'))
