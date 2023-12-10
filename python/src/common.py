from collections import deque
from types import GeneratorType
from typing import Callable
from time import perf_counter
from functools import wraps


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
    def inner_func(func: Callable) -> Callable:
        @wraps(func)
        def wrapped_func(*args, **kwargs):
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
                f"Elapsed time for {func.__name__.ljust(50,'.')}avg = {(elapsed_time/executions)*1000:.3f}ms.")
            return return_val
        return wrapped_func
    return inner_func
