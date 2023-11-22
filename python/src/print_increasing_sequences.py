# Print all increasing sequences of length k from first n natural nums
import itertools


def print_increasing_sequences(n: int, k: int):
    possible_combinations = 1 << n
    smallest_combination = (1 << k)-1
    for i in range(smallest_combination, possible_combinations):
        if bin(i).count('1') == k:
            # num-1 to start from binary 1(1<<1-1 = 1)
            print([num for num in range(1, n+1)
                   if 1 << (num-1) & i != 0])


def print_increasing_sequences_gosper(n: int, k: int):
    combination = (1 << k)-1
    possible_combinations = 1 << n
    while combination < possible_combinations:
        print([num for num in range(1, n+1)
              if 1 << (num-1) & combination != 0])

        rightmost_one_bit = combination & -combination
        left_side = combination + rightmost_one_bit
        ones_cluster = combination ^ left_side
        right_shifted = (ones_cluster >> 2)//rightmost_one_bit
        combination = right_shifted | left_side


def print_increasing_sequences_rec(n: int, k: int):
    def helper(num=1, seq=[]):
        if len(seq) == k:
            print(seq)
            return

        if num > n:
            return

        helper(num+1, seq+[num])
        helper(num+1, seq)

    helper()


# BONUS
print(list(itertools.combinations(range(1, 4), 2)))
