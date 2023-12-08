# Given two sorted arrays A and B, generate all possible arrays
# such that the first element is taken from A then from B then from A,
# and so on in increasing order till the arrays are exhausted.
# The generated arrays should end with an element from B.

from common import time_execution


@time_execution()
def generate_ascending_arrays_from_arrays_rec(A, B):
    result = []
    len_A = len(A)
    len_B = len(B)

    def helper(idx_a: int, idx_b: int, is_A_turn: bool, last_used: int,
               current_array: list[int]):

        if is_A_turn:
            for i in range(idx_a, len_A):
                if A[i] > last_used:
                    helper(i+1, 0, not is_A_turn,
                           A[i], current_array + [A[i]])
        else:
            for i in range(idx_b, len_B):
                if B[i] > last_used:
                    new_array = current_array + [B[i]]
                    result.append(new_array)
                    helper(0, i+1, not is_A_turn,
                           B[i], new_array)
    helper(0, 0, True, float('-inf'), [])
    return result


A = [10, 15, 25]
B = [1, 5, 20, 30]
print(generate_ascending_arrays_from_arrays_rec(A, B))
