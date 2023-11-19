from collections import deque
from types import GeneratorType


def consume(iter):
    deque(iter, maxlen=0)


def tramp(gen, *args, **kwargs):
    g = gen(*args, **kwargs)
    while isinstance(g, GeneratorType):
        g = next(g)
    return g
