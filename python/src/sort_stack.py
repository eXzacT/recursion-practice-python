# Sort a stack using recursion
from typing import TypeVar
from common import time_execution, tramp

# Any sortable type
T = TypeVar('T', int, float, str, list, tuple, range, set,
            frozenset, dict, bool, bytes, bytearray, memoryview)


@time_execution()
def sort_stack_rec(stack: list[T]) -> list[T]:
    def insert_sorted(stack: list[T], item: T) -> list[T]:
        # Top item smaller than the item or stack's empty
        if not stack or item > stack[-1]:
            stack.append(item)
        else:  # Pop the larger number from the stack, sort and then append it
            temp = stack.pop()
            insert_sorted(stack, item)
            stack.append(temp)

    def helper(stack: list[T]) -> list[T]:
        if not stack:
            return stack
        top = stack.pop()
        helper(stack)
        insert_sorted(stack, top)
        return stack

    return helper(stack)


print(sort_stack_rec([1, 2, 3, 1, 2, 3, 4, 5, 1, 7]))
