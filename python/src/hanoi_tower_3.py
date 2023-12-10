# Recursive Tower of Hanoi,3 rods
from common import time_execution


@time_execution(executions=1)
# If there's more than 1 execution then there will be duplicate prints
# Time_execution decorator is running the function 10 times for benchmarks
# Alternative is appending those prints to list instead
def hanoi_3(n: int) -> None:
    rods = {'A': [i for i in range(n, 0, -1)], 'B': [], 'C': []}

    def move_from(source: str, target: str):
        disk = rods[source].pop()
        print(f"Moving disk {disk} from {source} to {target}")
        rods[target].append(disk)

    def helper(n: int, source: str, aux: str, target: str):
        if n == 1:
            move_from(source, target)
        else:
            helper(n-1, source, target, aux)
            move_from(source, target)
            helper(n-1, aux, source, target)

    helper(n, 'A', 'B', 'C')


@time_execution(executions=1)
def hanoi_3_v2(n: int):
    def helper(n: int, start: int, end: int):
        def move_from(disk: int, start: int, end: int):
            print(f"Moving disk {disk} from rod {start} to rod {end}")

        if n == 1:
            move_from(n, start, end)
            return

        other = 6-(start+end)
        helper(n-1, start, other)
        move_from(n, start, end)
        helper(n-1, other, end)

    helper(n, 1, 3)


hanoi_3(3)
hanoi_3_v2(3)
