# Mean of Array using Recursion
from common import tramp


def array_mean_rec(arr: list, acc=0, total_nums=0) -> float:
    if not arr:
        return acc/total_nums
    curr = arr[0]
    return array_mean_rec(arr[1:], acc+curr, total_nums+1)


def array_mean_rec_idx(arr: list) -> float:
    length = len(arr)

    def helper(idx: int, acc=0):
        if idx >= length:
            return acc/length
        # Also not using slices, saves memory
        return helper(idx+1, acc + arr[idx])

    return helper(0)


def array_mean_rec_gen(arr: list, acc=0, total_nums=0) -> float:
    if not arr:
        yield acc/total_nums
    curr = arr[0]
    yield array_mean_rec_gen(arr[1:], acc+curr, total_nums+1)


def array_mean_rec_idx_gen(arr: list) -> float:
    # No need to count length since we pass it in the first call to a helper func
    length = len(arr)

    def helper(idx: int, acc=0):
        if idx >= length:
            yield acc/length
        # Also not using slices, saves memory
        yield helper(idx+1, acc + arr[idx])

    yield helper(0)


print(array_mean_rec([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(array_mean_rec_idx([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(array_mean_rec([i for i in range(10_000)]))
print(tramp(array_mean_rec_gen, [i for i in range(10_000)]))
print(tramp(array_mean_rec_idx_gen, [i for i in range(10_000)]))
