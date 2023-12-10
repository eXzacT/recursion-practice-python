# Recursive Tower of Hanoi, 4 rods
from common import time_execution


@time_execution()
def hanoi_4(n: int) -> None:
    rods = {'A': [i for i in range(n, 0, -1)], 'B': [], 'C': [], 'D': []}

    def move_from(source: str, target: str):
        disk = rods[source].pop()
        print(f"Moving {disk} from {source} to {target}")
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


hanoi_4(5)
