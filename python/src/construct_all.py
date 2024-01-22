# Return all the ways to construct a target string using words from a list of strings
from common import time_execution


@time_execution()
def all_construct_tabulation(target: str, word_bank: list[str]) -> list[list[str]]:
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for idx in range(len(target)):
        if table[idx]:
            for word in word_bank:
                if target[idx:idx+len(word)] == word:
                    new_combinations = [combination + [word]
                                        for combination in table[idx]]
                    table[idx+len(word)] += new_combinations

    return table[-1]


@time_execution()
def all_construct_rec(target: str, word_bank: list[str]) -> list[list[str]]:
    all_constructs = []

    def helper(target: str, construct=[]) -> None:
        if target == '':
            all_constructs.append(construct)
            return

        for word in word_bank:
            if target.startswith(word):
                helper(target[len(word):], construct+[word])

    helper(target)
    return all_constructs


@time_execution()
def all_construct_rec_memo(target: str, word_bank: list[str]) -> list[list[str]]:
    all_constructs = []
    memo = {'': None}
    memo_count = 0

    def helper(target: str, construct=[]) -> None:
        nonlocal memo_count
        if target in memo:
            memo_count += 1
            all_constructs.append(construct)
            return

        for word in word_bank:
            if target.startswith(word):
                memo[target] = helper(target[len(word):], construct+[word])

        memo[target] = None
        return

    helper(target)
    return f"{all_constructs}, memo_count: {memo_count}"


@time_execution()
def all_construct_rec_v2(target: str, word_bank: list[str]) -> list[list[str]]:
    word_bank_len = len(word_bank)
    all_constructs = []

    def helper(target: str, idx: int, construct=[]) -> None:
        if target == '':
            all_constructs.append(construct)
            return
        if idx == word_bank_len:
            return

        curr_word = word_bank[idx]
        if target.startswith(curr_word):  # 0 Because we have to consider all words
            helper(target[len(curr_word):], 0, construct+[curr_word])
        helper(target, idx+1, construct)

    helper(target, 0)
    return all_constructs


print(all_construct_tabulation("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(all_construct_rec("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(all_construct_rec_memo("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(all_construct_rec_v2("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
