# All possible combinations of n elements from a given array

def generate_n_sized_sets(n: int, arr: list[int]) -> list[list[int]]:
    length = len(arr)
    possible_combinations = 1 << length
    smallest_combination = 1 << n-1
    combinations = []

    for i in range(smallest_combination, possible_combinations):

        i_bin = bin(i)
        # Only keep going if we can actually form a set of n elements
        if i_bin.count('1') == n:
            print(i_bin)
            # Convert i to binary, remove the '0b' prefix
            # i_bin_str = i_bin[2:].zfill(len(arr))

            # Convert binary string to a list of integers (0s and 1s)
            # i_bin_list = [int(bin_digit) for bin_digit in i_bin_str]
            # combination = list(itertools.compress(arr, i_bin_list))
            combination = [arr[idx] for idx in range(i)
                           if 1 << idx & i != 0]
            combinations.append(combination)

    return combinations


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
