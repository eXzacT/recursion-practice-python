# Power Set in Lexicographic order

def lexicographic_power_set(arr: list[int]) -> list[list[int]]:
    power_set = [[]]
    for elem in arr:
        power_set += [subset + [elem] for subset in power_set]

    power_set.sort()
    return power_set


def lexicographic_power_set_bitwise(arr: list[int]) -> list[list[int]]:
    power_set = [[]]
    arr.sort()
    arr_len = len(arr)
    subset = 1 << arr_len-1
    # 1000  1100 1110 1111 1101 1010 1011 1001
    #  8     12   14   15   13   10    11   9

    # 0100  0110 0111 0101
    #   4    6     7    5

    # 0010 0011
    #   2    3

    # 0001
    #   1
    while subset > 1:
        for i in range(arr_len):
            power_set.append([arr[idx]]
                             for idx in range(arr_len) if (idx & subset) != 0)
            # change subset to be 1100 then 1110 then 1111 then 1101 etc

    return power_set


def lexicographic_power_set_bitwise_sort(arr: list[int]) -> list[list[int]]:
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


print(lexicographic_power_set([1, 2, 3, 4]))
print(lexicographic_power_set_bitwise([1, 2, 3, 4]))
print(lexicographic_power_set_bitwise_sort([1, 2, 3, 4]))
