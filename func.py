def func(x: int, y: int) -> None:
    print(f"{x} + {y} = {x+y}")

    if (x+y) <= ((x//10 + 1) * 10):
        return

    def find_combinations(n):
        combinations = []
        for i in range(1, n):
            if (i > n-i):
                break
            combinations.append([i, n-i])
        return combinations

    def find_res(x, combinations):
        for combination in combinations:
            if (combination[0] + x) % 10 == 0 and combination[0] <= 10:
                return (combination[0], combination[1])
            if (combination[1] + x) % 10 == 0 and combination[1] <= 10:
                return (combination[1], combination[0])
        return None

    res = (0, y)
    prev_nums = [y]
    while res[1] > 10:
        combinations = find_combinations(res[1])
        res = find_res(x, combinations)
        prev_nums[-1] = res[0]
        prev_nums.append(res[1])
        print(f"{x} + {' + '.join(map(str, prev_nums))} = {x+sum(prev_nums)}")
        x = x+res[0]
        prev_nums = prev_nums[1:]

    if res[1] <= 10:
        print(f"{x} + {' + '.join(map(str, prev_nums))} = {x+sum(prev_nums)}")


func(15, 18)
