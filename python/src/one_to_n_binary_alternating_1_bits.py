# 1 to n bit numbers with no consecutive 1s in binary representation
from common import time_execution


@time_execution()
def generate_no_consecutive_ones(n: int) -> list[str]:
    if n <= 0:
        return ['']

    binary_arr = ['0']
    num = 1
    while num < 1 << n:
        bin_num = bin(num)[2:]
        if '11' not in bin_num:
            binary_arr.append(bin_num)
        num += 1

    return binary_arr


@time_execution()
def generate_no_consecutive_ones_v2(n: int) -> list[str]:
    if n <= 0:
        return ['']

    ending_in_0 = ['0']
    ending_in_1 = ['1']

    for _ in range(1, n):
        # New strings ending in 0 are previous strings ending in 0 or 1 followed by 0
        new_ending_in_0 = [s + '0' for s in ending_in_0 + ending_in_1]

        # New strings ending in 1 are previous strings ending in 0 followed by 1
        new_ending_in_1 = [s + '1' for s in ending_in_0]

        ending_in_0, ending_in_1 = new_ending_in_0, new_ending_in_1

    return ending_in_0 + ending_in_1


@time_execution()
def generate_no_consecutive_ones_rec(n: int) -> list[str]:
    if n <= 0:
        return ['']

    binary_arr = ['0']

    def helper(base):
        if len(base) > n:
            return

        if base.count('1') >= 1:
            temp = base.lstrip('0')
            if temp not in binary_arr:
                binary_arr.append(temp)

        # Add 0 for both cases, only add '1' if it's currently '0'
        helper('0'+base)
        if base[0] == '0':
            helper('1'+base)

    helper('0')
    helper('1')

    return binary_arr


print(generate_no_consecutive_ones(4))
print(generate_no_consecutive_ones_v2(4))
print(generate_no_consecutive_ones_rec(4))
