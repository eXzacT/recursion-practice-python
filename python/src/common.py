import sys
from typing import Any
from collections import deque
from types import GeneratorType
from typing import Callable
from time import perf_counter
from functools import wraps

sys.stdout.reconfigure(encoding='utf-8')


def consume(iter):
    deque(iter, maxlen=0)


def tramp(gen, *args, **kwargs):
    '''
    Redundant if using @time_execution decorator with (isTrampoline=True)
    But without the decorator need to use tramp(func,args)
    '''
    g = gen(*args, **kwargs)
    while isinstance(g, GeneratorType):
        g = next(g)
    return g


def time_execution(isTrampoline: bool = False, executions: int = 10) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed_time = 0
            return_val = None
            for _ in range(executions):
                start = perf_counter()
                if isTrampoline:  # If it's a generator function
                    gen = func(*args, **kwargs)
                    while isinstance(gen, GeneratorType):
                        gen = next(gen)
                    return_val = gen
                else:
                    return_val = func(*args, **kwargs)
                end = perf_counter()
                elapsed_time += end - start
            print(
                f"Elapsed time for {func.__name__.ljust(50,'.')}avg = {(elapsed_time/executions)*1000:.4f}ms of {executions} times.")
            return return_val
        return wrapper
    return decorator


class RecursionTree:
    def __init__(self):
        self.call: str = ''
        self.returned: Any = None
        self.children: list[RecursionTree] = []

    def printTree(self, indent: str = ''):
        if self is None or len(self.children) == 0:
            print(self.call + ' returned ' + str(self.returned))
        else:
            print(self.call + ' returned ' + str(self.returned))
            for child in self.children[:-1]:
                print(indent + '|' + '-' * 4, end='')
                child.printTree(indent + '|' + ' ' * 4)
            child = self.children[-1]
            print(indent + '└' + '-' * 4, end='')
            child.printTree(indent + '  ' * 4)
