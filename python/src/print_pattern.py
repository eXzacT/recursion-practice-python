# Print a diamond pattern using recursion
from common import time_execution


@time_execution(executions=1)
def pattern(n: int):
    total_rows = 2*n-1

    def helper(m: int):
        if m == total_rows+2:
            return total_rows
        print(' '*((total_rows-m)//2)+'*'*m+' '*((total_rows-m)//2))
        res = helper(m+2)-2
        print(' '*((total_rows-res)//2)+'*'*res+' '*((total_rows-res)//2))
        return res

    helper(1)


@time_execution(executions=1)
def pattern_tabulation(n: int):
    pattern = []

    # Compute the first half of the pattern
    for i in range(n):
        row = ' ' * (n - i - 1) + '*' * (2 * i + 1)
        pattern.append(row)

    for p in pattern:
        print(p)
    for idx in range(len(pattern)-1, -1, -1):
        print(pattern[idx])


@time_execution(executions=1)
def pattern_tabulation_v2(n: int):
    pattern = []

    # Compute the first half of the pattern
    for i in range(n):
        row = ' ' * (n - i - 1) + '*' * (2 * i + 1)
        pattern.append(row)

    for idx in range(len(pattern)*2):
        if idx == len(pattern):
            continue
        if idx > len(pattern):
            print(pattern[-1-(idx % len(pattern))])
        else:
            print(pattern[idx])


@time_execution(executions=1)
def pattern_tabulation_v3(n: int):
    pattern = []

    # Compute the first half of the pattern
    for i in range(n):
        row = ' ' * (n - i - 1) + '*' * (2 * i + 1)
        pattern.append(row)

    # Reverse the pattern for next half and skip last
    pattern += pattern[-2::-1]
    for line in pattern:
        print(line)


pattern(5)
pattern_tabulation(5)
pattern_tabulation_v2(5)
pattern_tabulation_v3(5)
