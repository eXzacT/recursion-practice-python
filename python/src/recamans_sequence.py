from common import time_execution


@time_execution()
def recamans_sequence_iter(n: int) -> int:
    seen = set([0, 1])

    if n <= 0:
        return 0
    if n == 1:
        return [0, 1]

    prev = 1
    for i in range(2, n+1):
        curr = prev-i
        if curr < 0 or curr in seen:
            curr = i+prev
        seen.add(curr)
        prev = curr

    return curr


@time_execution()
def recamans_sequence_dp(n: int) -> list[int]:
    if n == 1:
        return n

    seen = set([0, 1])
    table = [0]*(n+1)
    table[1] = 1
    for i in range(2, n+1):
        curr = table[i-1]-i
        if curr in seen or curr < 0:
            curr = table[i-1]+i

        table[i] = curr
        seen.add(curr)

    return table[n]


@time_execution()
def recamans_sequence_rec(n: int) -> list[int]:
    seen = set([0, 1])
    if n <= 0:
        return 0

    if n == 1:
        return 1

    def helper(m: int, prev: int):
        curr = prev-m
        if curr < 0 or curr in seen:
            curr = prev+m
        seen.add(curr)

        if m == n:
            return curr
        else:
            return helper(m+1, prev=curr)

    return helper(2, prev=1)


@time_execution(isTrampoline=True)
def recamans_sequence_gen(n: int) -> list[int]:
    seen = set([0, 1])
    if n <= 0:
        return 0

    if n == 1:
        return 1

    def helper(m: int, prev: int):
        curr = prev-m
        if curr < 0 or curr in seen:
            curr = prev+m
        seen.add(curr)

        if m == n:
            yield curr
        else:
            yield helper(m+1, prev=curr)

    return helper(2, prev=1)


print(recamans_sequence_iter(5))
print(recamans_sequence_dp(5))
print(recamans_sequence_rec(5))
print(recamans_sequence_gen(10_000))
