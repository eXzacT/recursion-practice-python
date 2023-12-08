# All possible combinations of n elements from a given array
from common import time_execution


@time_execution()
def generate_n_sized_sets(n: int, arr: list[int]) -> list[list[int]]:
    length = len(arr)
    possible_combinations = 1 << length
    smallest_combination = 1 << n-1
    combinations = []

    for i in range(smallest_combination, possible_combinations):

        i_bin = bin(i)
        # Only keep going if we can actually form a set of n elements
        if i_bin.count('1') == n:
            combination = [arr[idx] for idx in range(i)
                           if 1 << idx & i != 0]
            combinations.append(combination)

    return combinations


@time_execution()
def generate_n_sized_sets_gosper(n: int, arr: list[int]) -> list[list[int]]:
    length = len(arr)
    possible_combinations = 1 << length
    combination = (1 << n) - 1
    combinations = []
    while combination < possible_combinations:
        combinations.append([arr[idx] for idx in range(length)
                             if combination & (1 << idx)])
        rightmost_1_bit = combination & -combination
        left_side = rightmost_1_bit + combination
        ones_cluster = left_side ^ combination
        right_shifted = (ones_cluster >> 2) // rightmost_1_bit
        combination = left_side | right_shifted

    return combinations


@time_execution()
def generate_n_sized_sets_rec(n: int, arr: list[int]) -> list[list[int]]:
    length = len(arr)

    def helper(n: int, idx=0):
        if n == 0:
            return [[]]
        if idx == length:
            return []

        with_first = [[arr[idx]] + rest for rest in helper(n-1, idx+1)]
        without_first = helper(n, idx+1)
        return with_first + without_first

    return helper(n)


print(generate_n_sized_sets(5, [1, 2, 3, 4, 5, 1, 2, 3]))
print(generate_n_sized_sets_gosper(5, [1, 2, 3, 4, 5, 1, 2, 3]))
print(generate_n_sized_sets_rec(5, [1, 2, 3, 4, 5, 1, 2, 3]))
