from collections import deque
from types import GeneratorType
from typing import Callable
from time import perf_counter
from functools import wraps


def consume(iter):
    deque(iter, maxlen=0)


def tramp(gen, *args, **kwargs):
    g = gen(*args, **kwargs)
    while isinstance(g, GeneratorType):
        g = next(g)
    return g


def time_execution(isTrampoline: bool = False) -> Callable:
    def inner_func(func: Callable):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            start_time = perf_counter()

            return_val = func(*args, **kwargs)
            if isTrampoline:
                while isinstance(return_val, GeneratorType):
                    return_val = next(return_val)

            end_time = perf_counter()
            print(
                f"Elapsed time for {func.__name__.ljust(50,'.')}{(end_time-start_time)*1000:.3f}ms.")
            return return_val

        return wrapped_func
    return inner_func
