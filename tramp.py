from types import GeneratorType


def tramp(gen, *args, **kwargs):
    g = gen(*args, **kwargs)
    while isinstance(g, GeneratorType):
        g = next(g)
    return g
