# Recursive Tower of Hanoi,3 rods
from common import time_execution


@time_execution(executions=1)
# If there's more than 1 execution then there will be duplicate prints
# Alternative is appending those prints to list instead
def hanoi_3(n: int) -> None:
    rods = {'A': [i for i in range(n, 0, -1)], 'B': [], 'C': []}

    def move_from(source: str, target: str):
        print(
            f"Before: A={str(rods['A']).ljust(10,'.')}B={str(rods['B']).ljust(10,'.')}C={str(rods['C']).ljust(10,'.')}", end=' ')
        disk = rods[source].pop()
        rods[target].append(disk)
        print(
            f"After: A={str(rods['A']).ljust(10,'.')}B={str(rods['B']).ljust(10,'.')}C={str(rods['C']).ljust(10,'.')}")

    def helper(n: int, source: str, aux: str, target: str):
        '''
        Source is start rod, aux is auxiliary rod, and target is target rod
        '''
        if n == 1:
            move_from(source, target)
        else:
            helper(n-1, source, target, aux)
            move_from(source, target)
            helper(n-1, aux, source, target)

    helper(n, 'A', 'B', 'C')


hanoi_3(3)
