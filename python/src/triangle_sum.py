# Sum triangle from array
from common import time_execution


@time_execution()
def triangle_sum(arr: list[int]) -> list[list[int]]:
    sum_matrix = [arr]

    while len(arr) > 1:
        arr = [arr[idx]+arr[idx+1] for idx in range(len(arr)-1)]
        sum_matrix.append(arr)

    return sum_matrix


@time_execution()
def triangle_sum_rec(arr: list[int]) -> list[list[int]]:
    row = arr
    sum_matrix = [row]

    def helper(idx=0):
        if idx == len(row)-1:
            return curr_row
        curr_row.append(row[idx]+row[idx+1])
        return helper(idx+1)

    while len(row) > 1:
        curr_row = []
        row = helper()
        sum_matrix.append(row)

    return sum_matrix


@time_execution()
def triangle_sum_tail_rec(arr: list[int]) -> list[list[int]]:
    sum_matrix = [arr]

    def helper(arr):
        row = []
        if len(arr) == 1:
            return sum_matrix

        for i in range(len(arr)-1):
            row.append(arr[i]+arr[i+1])

        sum_matrix.append(row)
        return helper(row)

    return helper(arr)


@time_execution(isTrampoline=True)
def triangle_sum_tail_gen(arr: list[int]) -> list[list[int]]:
    sum_matrix = [arr]

    def helper(arr):
        arr_len = len(arr)
        row = []

        if arr_len == 1:
            yield sum_matrix

        for i in range(arr_len-1):
            row.append(arr[i]+arr[i+1])

        sum_matrix.append(row)
        yield helper(row)

    return helper(arr)


print(triangle_sum([1, 2, 3, 4, 5]))
print(triangle_sum_rec([1, 2, 3, 4, 5]))
print(triangle_sum_tail_rec([1, 2, 3, 4, 5]))
print(triangle_sum_tail_gen([num for num in range(800)]))
