# Find the minimum (or maximum) element of an array

import functools
from typing import Callable, TypeVar

T = TypeVar('T')


def create_array_func(predicate: Callable[[T, T], bool]) -> Callable[[list[T]], T]:
    def array_num_func(arr: list[T]) -> T:
        return functools.reduce(lambda a, b: a if predicate(a, b) else b, arr)
    return array_num_func


max_array = create_array_func(lambda a, b: a > b)
min_array = create_array_func(lambda a, b: a < b)

print(max_array([1, 2, 3, 4, 5]))
print(min_array([1, 2, 3, 4, 5]))
print(min_array(['e', 'l', 'c', 'd']))
print(max_array(['a', 'z', 'd', 'f']))


def create_array_func_tail_rec(predicate: Callable[[T, T], bool]) -> Callable[[list[T]], T]:
    def array_num_func(arr: list[T]) -> T:
        arr_len = len(arr)
        curr_max = arr[0]

        def helper(idx=1) -> T:
            nonlocal curr_max
            if (idx == arr_len):
                return curr_max
            curr_max = curr_max if predicate(curr_max, arr[idx]) else arr[idx]
            return helper(idx+1)

        return helper()

    return array_num_func


max_array = create_array_func_tail_rec(lambda a, b: a > b)
min_array = create_array_func_tail_rec(lambda a, b: a < b)

print(max_array([1, 2, 3, 4, 5]))
print(min_array([1, 2, 3, 4, 5]))
print(min_array(['e', 'l', 'c', 'd']))
print(max_array(['a', 'z', 'd', 'f']))
