# Sort a stack using recursion
from common import time_execution
from typing import Any
import string


# @time_execution(executions=1)
@time_execution()
def reverse_stack_iter(stack: list[Any]) -> list[Any]:
    stack = stack.copy()  # As I explained below this is not necessary if run once
    reversed_stack = []
    while stack:
        reversed_stack.append(stack.pop())

    return reversed_stack


@time_execution()
def reverse_stack_rec(stack: list[Any]) -> list[Any]:
    def helper(stack: list[Any], reversed_stack: list[Any]) -> list:
        stack = stack.copy()
        if not stack:
            return reversed_stack
        el = stack.pop()
        return helper(stack, reversed_stack+[el])

    return helper(stack, [])


@time_execution(isTrampoline=True, executions=1)
# Because we're mutating stack and running reverse_stack_gen 10 times by default
# Have to make a stack copy for it to work, this does impact the runtime unfairly
# Or use executions=1, to have it run once
def reverse_stack_gen(stack: list[Any]) -> list[Any]:
    def helper(stack: list[Any], reversed_stack: list[Any]) -> list[Any]:

        # stack = stack.copy()
        if not stack:
            yield reversed_stack
        else:
            el = stack.pop()
            yield helper(stack, reversed_stack+[el])

    return helper(stack, [])


repeated_alphabet = 500*[char for char in string.ascii_lowercase]
print(reverse_stack_iter([5, 6, 7, 9, 5, 6, 7]))
print(reverse_stack_rec([5, 6, 7, 9, 5, 6, 7]))
# print(reverse_stack_rec(repeated_alphabet))
print(reverse_stack_gen(repeated_alphabet))
