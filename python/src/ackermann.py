if __name__ == "__main__":
    from common import time_execution, RecursionTree
else:
    from src.common import time_execution, RecursionTree


@time_execution()
def ackermann_dp(m: int, n: int) -> int:
    '''Doesn't work for ('m',0), not sure how to fix it'''
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:  # Base case 1: A(0, n) = n+1
                dp[0][j] = j + 1
            elif j == 0:  # Base case 2: A(m, 0) = A(m-1, 1)
                dp[i][0] = dp[i-1][1]
            else:
                row = i - 1
                col = dp[i][j-1]  # A(m, n-1) INNER recursive call
                if row == 0:  # Same as base case 1, since we subtracted 1 and got 0
                    res = col + 1
                # Recursive case: A(m, n) = A(m-1, INNER recursive call result)
                elif col <= n:  # Can fetch the value from the table
                    res = dp[i-1][col]
                else:  # Compute it using a formula because the value is not in the table
                    res = (col-n)*(row) + dp[row][n]

                dp[i][j] = res

    return dp[m][n]


@time_execution()
def ackermann_rec(m: int, n: int) -> int:
    def helper(m: int, n: int) -> int:
        if m == 0:
            return n+1
        if n == 0:
            return helper(m-1, 1)
        return helper(m-1, helper(m, n-1))

    return helper(m, n)


@time_execution()
def ackermann_memo(m: int, n: int) -> int:
    memo = {}

    def helper(m: int, n: int) -> int:
        key = (m, n)
        if key in memo:
            return memo[key]
        if m == 0:
            return n+1
        if n == 0:
            return helper(m-1, 1)

        memo[key] = helper(m-1, helper(m, n-1))
        return memo[key]

    return helper(m, n)


@time_execution(executions=1)
def recursion_tree(m: int, n: int, tree: RecursionTree) -> int:
    def helper(m: int, n: int, tree: RecursionTree) -> int:
        tree.call = 'ackerman_rec('+str(m)+','+str(n)+')'
        if m == 0:
            tree.returned = n+1
            return n+1
        if n == 0:
            child = RecursionTree()
            tree.children.append(child)
            res = helper(m-1, 1, child)
            tree.returned = res
            return res

        child = RecursionTree()
        tree.children.append(child)
        res = helper(m-1, helper(m, n-1, child), child)
        tree.returned = res
        return res

    return helper(m, n, tree)


if __name__ == "__main__":
    print(ackermann_dp(5, 5))  # Blazingly fast
    print(ackermann_rec(3, 4))
    print(ackermann_memo(3, 4))

    tree = RecursionTree()
    recursion_tree(2, 2, tree)
    tree.printTree()
