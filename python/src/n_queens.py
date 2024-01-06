'''Given a positive integer n, how many ways can we put n queens on a chess board of size n*n
    in such way that the queens don't attack each other
'''

from common import time_execution


@time_execution()
def n_queens_rec(n: int) -> int:
    def can_place(pos: complex) -> bool:
        for i in range(int(pos.real)):  # From 0 to this position row, not incl
            if board[complex(i, pos.imag)]:  # Check above
                return False
            # Returning 0 by default if we go out of bounds
            if board.get(complex(i, pos.imag - (pos.real - i)), 0):  # Left diagonal
                return False
            if board.get(complex(i, pos.imag + (pos.real - i)), 0):  # Right diagonal
                return False
        return True

    def place_queen(row: int) -> int:
        if row == n:  # Managed to place all n queens
            return 1

        combinations = 0
        # Check if we can place the queen anywhere on this row
        for new_pos in [complex(row, j) for j in range(n)]:
            if can_place(new_pos):
                board[new_pos] = 1  # Place the queen
                combinations += place_queen(row+1)
                board[new_pos] = 0  # Remove the queen for backtracking

        return combinations

    board = {complex(i, j): 0 for i in range(n)
             for j in range(n)}
    return place_queen(0+0j)


@time_execution()
def n_queens_rec_v2(n: int) -> int:
    cols = [0 for _ in range(n)]
    major_diagonals = [0 for _ in range(2*n-1)]
    minor_diagonals = [0 for _ in range(2*n-1)]

    def place_queen(row: int) -> int:
        combinations = 0
        if row == n:  # Managed to place all n queens
            return 1
        for col in range(n):

            major_idx = n-1 - (row-col)
            minor_idx = row+col

            if not cols[col] and not major_diagonals[major_idx] and not minor_diagonals[minor_idx]:
                cols[col] = 1
                major_diagonals[major_idx] = 1
                minor_diagonals[minor_idx] = 1

                combinations += place_queen(row+1)

                cols[col] = 0
                major_diagonals[major_idx] = 0
                minor_diagonals[minor_idx] = 0

        return combinations

    return place_queen(0)


print(n_queens_rec(8))
print(n_queens_rec_v2(8))
