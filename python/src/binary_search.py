from common import time_execution


@time_execution()
def binary_search_iter(arr: list[int], needle: int) -> int:
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = lo+(hi-lo)//2
        if arr[mid] == needle:
            return mid
        if needle < arr[mid]:
            hi = mid-1
        else:
            lo = mid+1

    return -1


@time_execution()
def binary_search_rec(arr: list[int], needle: int) -> int:
    def helper(lo: int, hi: int) -> int:
        mid = lo+(hi-lo)//2
        if arr[mid] == needle:
            return mid
        if lo > hi:
            return -1
        if needle < arr[mid]:
            return helper(lo, mid-1)
        else:
            return helper(mid+1, hi)

    return helper(0, len(arr)-1)


print(binary_search_iter([1, 2, 6, 9, 23, 45, 122, 419], 6))
print(binary_search_rec([1, 2, 6, 9, 23, 45, 122, 419], 6))
