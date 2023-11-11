# Mean of Array using Recursion
from common import tramp


def array_mean_rec(arr: list, acc=0, total_nums=0) -> float:
    if not arr:
        return acc/total_nums
    curr = arr[0]
    return array_mean_rec(arr[1:], acc+curr, total_nums+1)


def array_mean_rec_gen(arr: list, acc=0, total_nums=0) -> float:
    if not arr:
        yield acc/total_nums
    curr = arr[0]
    yield array_mean_rec_gen(arr[1:], acc+curr, total_nums+1)


# print(array_mean_rec([i for i in range(10_000)]))
print(tramp(array_mean_rec_gen, [i for i in range(10_000)]))
