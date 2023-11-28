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


def time_execution(func: Callable) -> Callable:
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        start_time = perf_counter()
        return_val = func(*args, **kwargs)
        end_time = perf_counter()
        print(
            f"Elapsed seconds of the function {func.__name__} is {end_time-start_time}")
        return return_val

    return wrapped_func
