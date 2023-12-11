# Print all non-increasing sequences of sum equal to a given number x
from common import time_execution


@time_execution()
def non_increasing_sum_sequences_tabulation(num: int) -> list[list[int]]:
    table = [[] for _ in range(num + 1)]
    table[0] = [[]]  # Base case, 0 can be made with no nums

    for i in range(1, num + 1):  # Table range
        for j in range(i, num + 1):
            for seq in table[j - i]:
                table[j].append([i]+seq)

    return sorted(table[num], reverse=True)


@time_execution()
def non_increasing_sum_sequences_rec(num: int) -> list[list[int]]:
    sequences = []

    def helper(remainder: int, max_num: int, sequence=[]):
        if remainder == 0:
            sequences.append(sequence)
            return
        for i in range(min(max_num, remainder), 0, -1):
            helper(remainder-i, i, sequence+[i])

    helper(num, num)
    return sequences


@time_execution()
def non_increasing_sum_sequences_memo(num: int) -> list[list[int]]:
    memo = {}
    # memo_count = 0

    def helper(remainder: int, max_num: int) -> list[list[int]]:
        # nonlocal memo_count
        key = (remainder, max_num)

        if remainder == 0:
            return [[]]
        if key in memo:
            # memo_count += 1
            return memo[key]

        sequences = []
        for i in range(min(max_num, remainder), 0, -1):
            for seq in helper(remainder - i, i):
                sequences.append([i] + seq)

        memo[key] = sequences
        return sequences

    return helper(num, num)
    return f"{helper(num, num)}, memo count: {memo_count}"


print(non_increasing_sum_sequences_tabulation(5))
print(non_increasing_sum_sequences_rec(5))
print(non_increasing_sum_sequences_memo(5))
