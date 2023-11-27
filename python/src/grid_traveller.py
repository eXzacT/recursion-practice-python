# Traveller on a 2d grid, how many ways can you travel
# from top left to bottom right, can only move down or right

def grid_traveller_rec(m: int, n: int) -> int:
    if m == 0 or n == 0:
        return "Not a valid grid"

    def helper(start_m=1, start_n=1) -> int:
        if start_m == m and start_n == n:
            return 1
        if start_m == m:
            return helper(start_m, start_n+1)
        if start_n == n:
            return helper(start_m+1, start_n)
        return helper(start_m+1, start_n) + helper(start_m, start_n+1)
    return helper()


def grid_traveller_rec_v2(m: int, n: int) -> int:
    def helper(m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        return helper(m-1, n) + helper(m, n-1)

    return helper(m, n)


def grid_traveller_memo(m: int, n: int) -> int:
    def helper(m: int, n: int, memo={}) -> int:
        key = m + n
        if key in memo:
            return memo[key]
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1

        memo[key] = helper(m-1, n, memo) + helper(m, n-1, memo)
        return memo[key]

    return helper(m, n)


print(grid_traveller_rec(10, 10))
print(grid_traveller_rec_v2(10, 10))
print(grid_traveller_memo(30, 30))
