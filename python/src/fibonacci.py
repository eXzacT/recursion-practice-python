import sys
from common import time_execution, RecursionTree


@time_execution()
def fibonacci_iter(n: int) -> int:
    a = 0
    b = 1

    if n == 0:
        return 0
    if n == 1:
        return 1

    for _ in range(2, n+1):
        a, b = b, a+b
    return b


@time_execution()
def fibonacci_dp(n: int) -> int:
    if n == 0:
        return 0
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n]


@time_execution()
def fibonacci_dp_v2(n: int) -> int:
    if n == 0:
        return 0
    prevprev = 0
    prev = 1
    for _ in range(2, n+1):
        prevprev, prev = prev, prevprev+prev

    return prev


@time_execution()
def fibonacci_rec(n: int) -> int:
    def helper(n: int) -> int:
        if n <= 1:
            return n
        return helper(n-1) + helper(n-2)

    return helper(n)


@time_execution()
def fibonacci_memo(n: int) -> int:
    memo = {0: 0, 1: 1}

    def helper(n: int) -> int:
        if n in memo:
            return memo[n]
        memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
        return memo[n]
    return helper(n)


@time_execution()
def fibonacci_tail_rec(n: int) -> int:
    def helper(n: int, curr=0, nxt=1):
        if n == 0:
            return curr
        return helper(n-1, nxt, curr+nxt)

    return helper(n)


@time_execution(isTrampoline=True)
def fibonacci_gen(n: int) -> int:
    def helper(n: int, curr=0, nxt=1):
        if n == 0:
            yield curr
        else:
            yield helper(n-1, nxt, curr+nxt)
    return helper(n)


print(fibonacci_iter(10))
print(fibonacci_dp(10))
print(fibonacci_dp_v2(10))
print(fibonacci_rec(10))
print(fibonacci_tail_rec(10))

sys.set_int_max_str_digits(500_000)
print(fibonacci_gen(100_000))


@time_execution(executions=1)
def fibonacci_rec(n: int, tree: RecursionTree) -> int:
    # Visualization
    def helper(n: int, tree: RecursionTree):
        tree.call = 'fibonacci_rec('+str(n)+')'
        if n <= 1:
            tree.returned = n
            return n

        child1 = RecursionTree()
        tree.children.append(child1)
        res1 = helper(n-1, child1)

        child2 = RecursionTree()
        tree.children.append(child2)
        res2 = helper(n-2, child2)

        res = res1 + res2
        tree.returned = res
        return res

    return helper(n, tree)


tree = RecursionTree()
fibonacci_rec(5, tree)
tree.printTree()
