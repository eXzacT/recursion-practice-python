# Mean of Array using Iteration and Recursion
from functools import reduce
from operator import add

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


@time_execution()
def array_mean(arr: list) -> float:
    arr_sum = 0
    for el in arr:
        arr_sum += el
    return arr_sum/len(arr)


@time_execution()
def array_mean_reduce(arr: list) -> float:
    return reduce(add, arr)/len(arr)


@time_execution()
def array_mean_rec(arr: list[int]) -> float:
    def helper(idx: int):
        if idx == len(arr):
            return 0
        return arr[idx]+helper(idx+1)
    return helper(0)/len(arr)


@time_execution()
def array_mean_tail_rec(arr: list[int]) -> float:
    def helper(arr: list[int], acc: int = 0, total_nums: int = 0) -> float:
        if not arr:
            return acc/total_nums
        curr = arr[0]
        return helper(arr[1:], acc+curr, total_nums+1)
    return helper(arr)


@time_execution()
def array_mean_tail_rec_v2(arr: list) -> float:
    def helper(idx: int = 0, acc: int = 0) -> float:
        if idx == len(arr):
            return acc/len(arr)
        return helper(idx+1, acc + arr[idx])

    return helper()


@time_execution(isTrampoline=True)
def array_mean_gen(arr: list) -> float:
    def helper(idx: int = 0, acc: int = 0):
        if idx == len(arr):
            yield acc/len(arr)
        yield helper(idx+1, acc + arr[idx])

    yield helper()


if __name__ == "__main__":
    arr = [i for i in range(1, 100)]
    print(array_mean(arr))
    print(array_mean_reduce(arr))
    print(array_mean_rec(arr))
    print(array_mean_tail_rec(arr))
    print(array_mean_tail_rec_v2(arr))
    # print(array_mean_rec([i for i in range(10_000)]))
    print(array_mean_gen([i for i in range(1, 10_001)]))
