from common import time_execution

'''Given an input string of numbers such as 374 give all the possible combinations for this keypad
1(.)    2(ABC) 3(DEF)
4(GHI)  5(JKL) 6(MNO)
7(PQRS) 8(TUV) 9(WXYZ)
        0(+)
'''

keypad = ["+", ".", "ABC", "DEF", "GHI",  "JKL", "MNO", "PQRS", "TUV", "WXYZ",]


@time_execution()
def keypad_combinations(keys: str) -> list[str]:
    combinations = []

    def helper(i: int, j: int, combination: str = "") -> None:
        if i == len(keys):
            combinations.append(combination)
            return

        key = int(keys[i])
        letters = keypad[key]
        if j == len(letters):
            return

        helper(i+1, 0, combination+letters[j])
        helper(i, j+1, combination)

    helper(0, 0)
    return combinations


@time_execution()
def keypad_combinations_v2(keys: str) -> list[str]:
    combinations = []

    def helper(i: int, combination: list[str] = []) -> None:
        if i == len(keys):
            combinations.append(''.join(combination))
            return

        key = int(keys[i])
        for letter in keypad[key]:
            combination.append(letter)
            helper(i+1, combination)
            combination.pop()

    helper(0)
    return combinations


@time_execution()
def keypad_combinations_v3(keys: str) -> list[str]:
    combinations = []

    def helper(idx: int, combination: str = "") -> None:
        if idx == len(keys):
            combinations.append(combination)
            return

        key = int(keys[idx])
        for letter in keypad[key]:
            helper(idx+1, combination+letter)

    helper(0)
    return combinations


@time_execution()
def keypad_combinations_v4(keys: str) -> list[str]:
    def helper(idx: int) -> None:
        key = int(keys[idx])
        # Start building the combinations when going backwards from recursion
        if idx == len(keys)-1:
            return keypad[key]

        from_next = helper(idx+1)
        combinations = []
        for letter in keypad[key]:
            for combination in from_next:
                combinations.append(letter+combination)

        return combinations

    return helper(0)


print(keypad_combinations("374"))
print(keypad_combinations_v2("374"))
print(keypad_combinations_v3("374"))
print(keypad_combinations_v4("374"))
