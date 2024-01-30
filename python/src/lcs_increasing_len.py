'''Given an array 'arr', find the length of the longest strictly increasing subsequence'''
from common import time_execution
import networkx as nx
import bisect


@time_execution()
def increasing_lcs_len_dp(arr: list[int]) -> int:
    # Longest len by taking the first element itself is 1
    dp = [0]*len(arr)
    dp[0] = 1
    for i in range(1, len(arr)):
        # We can only add the curr number to arrays where last number used was smaller than curr
        # So we take the maxlen stored at that index in dp and increment by 1
        dp[i] = 1+max(dp[j] for j in range(i) if arr[i] > arr[j])

    return max(dp)


@time_execution()
def increasing_lcs_len_rec(arr: list[int]) -> int:
    def helper(idx: int, prev: int) -> int:
        if idx == len(arr):
            return 0

        # At every step we can either take the number(if possible) or not take the number
        if arr[idx] > prev:
            return max(helper(idx+1, prev), 1+helper(idx+1, arr[idx]))
        return helper(idx+1, prev)

    return helper(0, float('-inf'))


@time_execution()
def increasing_lcs_len_memo(arr: list[int]) -> int:
    memo = {}
    memo_hits = 0

    def helper(i: int, prev: int) -> int:
        nonlocal memo_hits
        key = (i, prev)

        if i == len(arr):
            return 0
        if key in memo:
            memo_hits += 1
            return memo[key]

        # At every step we can either take the number(if possible) or not take the number
        if arr[i] > prev:
            memo[key] = max(helper(i+1, prev), 1+helper(i+1, arr[i]))
            return memo[key]

        memo[key] = helper(i+1, prev)
        return memo[key]

    return f"{helper(0, float('-inf'))}, memo_hits: {memo_hits}"


@time_execution()
def increasing_lcs_len_rec_v2(arr: list[int]) -> int:
    def helper(idx: int) -> int:
        maxlen = 0
        for i in range(idx+1, len(arr)):
            if arr[i] > arr[idx]:
                maxlen = max(maxlen, helper(i))
        return 1 + maxlen

    return max(helper(idx) for idx in range(len(arr)))


@time_execution()
def increasing_lcs_len_memo_v2(arr: list[int]) -> int:
    memo = {}
    memo_hits = 0

    def helper(idx: int) -> int:
        nonlocal memo_hits
        if idx in memo:
            memo_hits += 1
            return memo[idx]

        maxlen = 0
        for i in range(idx+1, len(arr)):
            if arr[i] > arr[idx]:
                maxlen = max(maxlen, helper(i))

        memo[idx] = maxlen+1
        return memo[idx]

    return f"{max(helper(idx) for idx in range(len(arr)))}, memo_hits={memo_hits}"


@time_execution()
def increasing_lcs_len_nx(arr: list[int]) -> int:
    G = nx.DiGraph()

    def helper(idx: int) -> None:
        if idx == len(arr):
            return

        for i in range(idx+1, len(arr)):
            if arr[i] > arr[idx]:
                G.add_edge(idx, i)
                helper(i)

    for i in range(len(arr)):
        helper(i)

    return 1+nx.dag_longest_path_length(G)


@time_execution()
def increasing_lcs_len_bisect(arr: list[int]) -> int:
    stacks = []
    for num in arr:
        idx = bisect.bisect_left(stacks, num)
        if idx == len(stacks):
            stacks.append(num)
        else:
            stacks[idx] = num

    return len(stacks)


nums = [2, 5, 10, 20, 3, 4, 5, 9, 10, 23, 42, 12, 34, 52, 12]
print(increasing_lcs_len_dp(nums))
print(increasing_lcs_len_rec(nums))
print(increasing_lcs_len_memo(nums))
print(increasing_lcs_len_rec_v2(nums))
print(increasing_lcs_len_memo_v2(nums))
print(increasing_lcs_len_nx(nums))
print(increasing_lcs_len_bisect(nums))
