# Power Set in Lexicographic order
from common import time_execution


@time_execution()
def lexicographic_power_set(arr: list) -> list[list]:
    power_set = [[]]
    for elem in arr:
        power_set += [subset + [elem] for subset in power_set]

    power_set.sort()
    return power_set


@time_execution()
def lexicographic_power_set_bitwise(arr: list[int]) -> list[list[int]]:
    power_set = []
    length = len(arr)
    for i in range(1 << length):
        subset = []
        for j in range(length):
            if i & (1 << j):
                subset.append(arr[j])
        power_set.append(subset)
    power_set.sort()
    return power_set


@time_execution()
def lexicographic_power_set_rec(arr: list) -> list[list]:
    def helper(arr: list) -> list[list]:
        if len(arr) == 0:
            return [[]]

        subsets = helper(arr[1:])
        return sorted(subsets + [[arr[0]] + subset for subset in subsets])
    return helper(arr)


@time_execution()
def lexicographic_power_set_rec_v2(arr: list) -> list[list]:
    arr_len = len(arr)

    def helper(idx=0, power_set=[[]]):
        if idx == arr_len:
            return sorted(power_set)
        power_set += [subset+[arr[idx]] for subset in power_set]
        return helper(idx+1, power_set)

    return helper()


print(lexicographic_power_set([1, 2, 3, 4, 5, 1]))
print(lexicographic_power_set_bitwise([1, 2, 3, 4, 5, 1]))
print(lexicographic_power_set_rec([1, 2, 3, 4, 5, 1]))
print(lexicographic_power_set_rec_v2([1, 2, 3, 4, 5, 1]))
