from typing import Callable, Any


def add(*x: int) -> int:
    return sum(x)


def multiply(x: int, y: int) -> int:
    return x*y


def subtract(x: int, y: int) -> int:
    return x-y


def curry(func: Callable[..., Any], *args: Any) -> Callable[..., Any]:
    def curried(*args2: Any) -> Any:
        return func(*args, *args2)
    return curried


def outerFunction():
    text = ""

    def innerFunction(new_txt):
        nonlocal text
        text = new_txt+text
        return text
    return innerFunction


my = outerFunction()
my("yoyo")
my("doyo")
my("froyo")
print(my("mojo"))
