from common import time_execution


@time_execution()
def merge_sort_iter(arr):
    size = len(arr)
    temp = [0] * size
    width = 1

    while width < size:
        for i in range(0, size, 2 * width):
            left = i
            right = min(i + 2 * width, size)
            mid = min(i + width, right)

            l, r, k = left, mid, left
            # Merge the two halves into temp
            while l < mid and r < right:
                if arr[l] < arr[r]:
                    temp[k] = arr[l]
                    l += 1
                else:
                    temp[k] = arr[r]
                    r += 1
                k += 1
            while l < mid:
                temp[k] = arr[l]
                l += 1
                k += 1
            while r < right:
                temp[k] = arr[r]
                r += 1
                k += 1
            # Copy the sorted elements back into original array
            for j in range(left, right):
                arr[j] = temp[j]
        width = 2 * width
    return arr


@time_execution()
def merge_sort_rec(arr: list[int]) -> list[int]:
    def join(arr1: list[int], arr2: list[int]) -> list[int]:
        merged_arr = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged_arr.append(arr1[i])
                i += 1
            else:
                merged_arr.append(arr2[j])
                j += 1

        # If any of the arrays are still not exhausted just add them to end
        merged_arr.extend(arr1[i:])
        merged_arr.extend(arr2[j:])

        return merged_arr

    def merge(arr: list[int]) -> list[int]:
        if len(arr) == 1:
            return arr

        mid = len(arr)//2
        return join(merge(arr[:mid]), merge(arr[mid:]))

    return merge(arr)


print(merge_sort_iter([3, 8, 419, 10, 23, 5, 72, 6]))
print(merge_sort_rec([3, 8, 419, 10, 23, 5, 72, 6]))
