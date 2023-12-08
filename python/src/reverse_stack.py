# Sort a stack using recursion
from common import time_execution, tramp
from typing import Any
import string


@time_execution()
def reverse_stack_iter(stack: list[Any]) -> list[Any]:
    reversed_stack = []
    while stack:
        reversed_stack.append(stack.pop())

    return reversed_stack


@time_execution()
def reverse_stack_rec(stack: list[Any]) -> list[Any]:
    def helper(stack: list[Any], reversed_stack: list[Any]) -> list:
        if not stack:
            return reversed_stack
        el = stack.pop()
        return helper(stack, reversed_stack+[el])

    return helper(stack, [])


@time_execution(isTrampoline=True)
def reverse_stack_gen(stack: list[Any]) -> list[Any]:
    def helper(stack: list[Any], reversed_stack: list[Any]) -> list[Any]:
        if not stack:
            yield reversed_stack
        el = stack.pop()
        yield helper(stack, reversed_stack+[el])

    return helper(stack, [])


repeated_alphabet = 1000*[char for char in string.ascii_lowercase]
print(reverse_stack_iter([5, 6, 7, 9, 5, 6, 7]))
print(reverse_stack_rec([5, 6, 7, 9, 5, 6, 7]))
# print(reverse_stack_rec(repeated_alphabet))
print(tramp(reverse_stack_gen, repeated_alphabet))
