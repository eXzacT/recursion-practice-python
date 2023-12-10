# Recursive Tower of Hanoi, 4 rods
from common import time_execution


@time_execution(executions=1)
# If there's more than 1 execution then there will be duplicate prints
# Time_execution decorator is running the function 10 times for benchmarks
# Alternative is appending those prints to list instead
def hanoi_4(n: int) -> None:
    rods = {'A': [i for i in range(n, 0, -1)], 'B': [], 'C': [], 'D': []}

    def move_from(source: str, target: str):
        disk = rods[source].pop()
        print(f"Moving disk {disk} from peg {source} to peg {target}")
        rods[target].append(disk)

    def helper(n: int, source: str, aux1: str, aux2: str, target: str):
        if n == 1:
            move_from(source, target)
        else:
            helper(n-2, source, target, aux2, aux1)
            move_from(source, aux2)
            move_from(source, target)
            move_from(aux2, target)
            helper(n-2, aux1, source, aux2, target)

    helper(n, 'A', 'B', 'C', 'D')


@time_execution(executions=1)
def hanoi_4_v2(n: int):
    def helper(n: int, source: str, aux1: str, aux2: str, target: str):
        def move_from(disk: int, source: str, target: str):
            print(f"Moving disk {disk} from peg {source} to peg {target}")
        if n == 1:
            move_from(n, source, target)
        else:
            helper(n-2, source, aux2, target, aux1)
            move_from(n-1, source, aux2)
            move_from(n, source, target)
            move_from(n-1, aux2, target)
            helper(n-2, aux1, source, aux2, target)

    return helper(n, 'A', 'B', 'C', 'D')


hanoi_4(5)
hanoi_4_v2(5)
