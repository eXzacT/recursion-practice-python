# Power Set in Lexicographic order

def lexicographic_power_set(arr: list) -> list[list]:
    power_set = [[]]
    for elem in arr:
        power_set += [subset + [elem] for subset in power_set]

    power_set.sort()
    return power_set


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


def lexicographic_power_set_rec(arr: list) -> list[list]:
    if len(arr) == 0:
        return [[]]

    subsets = lexicographic_power_set_rec(arr[1:])
    return sorted(subsets + [[arr[0]] + subset for subset in subsets])


def lexicographic_power_set_rec_v2(arr: list) -> list[list]:
    arr_len = len(arr)

    def helper(idx=0, power_set=[[]]):
        if idx == arr_len:
            return sorted(power_set)
        power_set += [subset+[arr[idx]] for subset in power_set]
        return helper(idx+1, power_set)

    return helper()
