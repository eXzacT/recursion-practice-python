# Mean of Array using Iteration and Recursion
from common import tramp
import itertools
import functools


def array_mean(arr: list) -> float:
    sum = 0
    for el in arr:
        sum += el
    return sum/len(arr)


def array_mean_rec(arr: list) -> float:
    length = len(arr)

    def helper(idx: int):
        if idx >= length:
            return 0
        return arr[idx]+helper(idx+1)
    return helper(0)/length


def array_mean_tail_rec(arr: list, acc=0, total_nums=0) -> float:
    if not arr:
        return acc/total_nums
    curr = arr[0]
    return array_mean_tail_rec(arr[1:], acc+curr, total_nums+1)


def array_mean_tail_rec_idx(arr: list) -> float:
    length = len(arr)

    def helper(idx: int, acc=0):
        if idx >= length:
            return acc/length
        # Also not using slices, saves memory
        return helper(idx+1, acc + arr[idx])

    return helper(0)


def array_mean_gen(arr: list) -> float:
    # No need to count length since we pass it in the first call to a helper func
    length = len(arr)

    def helper(idx: int, acc=0):
        if idx >= length:
            yield acc/length
        # Also not using slices, saves memory
        yield helper(idx+1, acc + arr[idx])

    yield helper(0)


arr = [i for i in range(1, 11)]
print(array_mean(arr))
print(array_mean_rec(arr))
print(array_mean_tail_rec(arr))
print(array_mean_tail_rec_idx(arr))
# print(array_mean_rec([i for i in range(10_000)]))
print(tramp(array_mean_gen, [i for i in range(1, 10_001)]))

print(list(itertools.accumulate(arr, lambda x, y: x+y))[len(arr)-1]/len(arr))
print(functools.reduce(lambda x, y: x+y, arr)/len(arr))
