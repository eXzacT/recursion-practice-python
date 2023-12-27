# Minimum tiles of sizes in powers of two to cover whole area
# 2x2 4x4 8x8 tiles ... etc to cover a m*n area
import math


def tiles_in_powers(m: int, n: int) -> list[int]:
    tiles = []

    def helper(m: int, n: int):
        if m == 0 or n == 0:
            return
        if m == 1 or n == 1:
            for _ in range(max(m, n)):
                tiles.append(1)  # Add tiles of 1x1 max amount of times
            return

        min_dimension = min(m, n)
        max_power = int(math.log2(min_dimension))
        max_tile = 1 << max_power
        tiles.append(max_tile)

        # Call it on the 2 remaining slices
        helper(m-max_tile, n)
        # Can't use m, because that space is used in previous call
        helper(max_tile, n-max_tile)

    helper(m, n)
    return tiles


print(tiles_in_powers(10, 5))
