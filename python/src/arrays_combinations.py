from common import time_execution


@time_execution()
def arrays_combinations_rec(arr: list[list[str]]) -> list[str]:
    combinations = []

    def helper(i: int, j: int, string_so_far: str) -> None:
        if i == len(arr):
            combinations.append(string_so_far)
            return
        if j >= len(arr[i]):
            return

        helper(i+1, j-j, string_so_far+" "+arr[i][j])
        helper(i, j+1, string_so_far)

    # By starting from 1 and every word in first array we can avoid having to do lstrip
    for word in arr[0]:
        helper(1, 0, word)

    return combinations


@time_execution()
def arrays_combinations_rec_v2(arr: list[list[str]]) -> list[str]:
    combinations = []

    def helper(i: int, words_so_far: list[str]) -> None:
        if i == len(arr):
            combinations.append(' '.join(words_so_far))
            return

        for word in arr[i]:
            words_so_far.append(word)
            helper(i+1, words_so_far)
            words_so_far.pop()

    helper(0, [])
    return combinations


@time_execution()
def arrays_combinations_rec_v3(arr: list[list[str]]) -> list[str]:
    combinations = []

    def helper(i: int, string_so_far: str) -> None:
        if i == len(arr):
            combinations.append(string_so_far)
            return

        for word in arr[i]:
            helper(i+1, string_so_far+" "+word)

    for word in arr[0]:
        helper(1, word)

    return combinations


@time_execution()
def arrays_combinations_rec_v4(arr: list[list[str]]) -> list[str]:
    def helper(i: int) -> None:
        if i == len(arr):
            return ['']

        next_sublist = helper(i+1)
        phrases = []
        # Add every word in the current sublist to the beginning of every phrase in the next list
        for word in arr[i]:
            for phrase in next_sublist:
                phrases.append(
                    word + (' ' if len(phrase) > 0 else '') + phrase)

        return phrases

    return helper(0)


@time_execution()
def arrays_combinations_rec_v5(arr: list[list[str]]) -> list[str]:
    def helper(i: int) -> None:
        if i == len(arr)-1:  # Return the final sublist
            return arr[i]

        next_sublist = helper(i+1)
        phrases = []
        # Add every word in the current sublist to the beginning of every phrase in the next list
        for word in arr[i]:
            for phrase in next_sublist:
                phrases.append(
                    word + ' ' + phrase)

        return phrases

    return helper(0)


arr = [["John", "Tom", "Jack"], ["cooks", "eats"],
       ["chicken", "rice", "spaghetti", "fish"]]

print(arrays_combinations_rec(arr))
print(arrays_combinations_rec_v2(arr))
print(arrays_combinations_rec_v3(arr))
print(arrays_combinations_rec_v4(arr))
print(arrays_combinations_rec_v5(arr))
