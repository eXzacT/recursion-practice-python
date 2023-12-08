# Given two numbers num and pow, find ways num can be expressed as
# sum of n-th power of unique natural numbers.
from pprint import pprint
from common import time_execution


@time_execution()
def sum_of_powers(num: int, pow: int) -> list[int]:
    res = []

    def helper(start_num=1, acc=0, temp=[]):
        if acc == num:
            res.append(temp)
            return
        if acc > num or start_num > num:
            return

        helper(start_num+1, acc, temp)
        helper(start_num+1, acc + start_num**pow,
               temp + [f"{start_num}^{pow}"])

    helper()
    return res


@time_execution()
def sum_of_powers_memo(num: int, pow: int) -> list[list[str]]:
    # TODO FIX
    memo = {}
    memo_count = 0

    def helper(start_num=1, acc=0, temp=[]):
        nonlocal memo_count
        key = acc
        if key in memo:
            memo_count += 1
            return memo[key]

        if acc == num:
            return [temp]
        if acc > num or start_num > num:
            return []

        without_curr = helper(start_num + 1, acc, temp)
        with_curr = helper(start_num + 1, acc + start_num **
                           pow, temp + [f"{start_num}^{pow}"])

        memo[key] = without_curr + with_curr
        return memo[key]

    return f"{helper()}, memo_count: {memo_count}"


pprint(sum_of_powers(14, 1))
pprint(sum_of_powers_memo(14, 1))
