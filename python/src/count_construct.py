# Return how to construct a target string using words from a list of strings
from common import time_execution


@time_execution
def count_construct_tabulation(target: str, word_bank: list[str]) -> int:
    target_len = len(target)
    table = [0 for _ in range(target_len+1)]
    table[0] = 1

    for idx in range(target_len+1):
        if table[idx] != 0:
            for word in word_bank:
                word_len = len(word)
                if target[idx:idx+word_len] == word:
                    table[idx+word_len] += table[idx]

    return table[-1]


@time_execution
def count_construct_rec(target: str, word_bank: list[str]) -> int:
    word_bank_len = len(word_bank)

    def helper(target: str, idx: int) -> int:
        if target == '':
            return 1
        if idx == word_bank_len:
            return 0

        if target.startswith(word_bank[idx]):
            with_word = helper(target.lstrip(word_bank[idx]), 0)
            without_word = helper(target, idx+1)
            return with_word+without_word
        else:
            return helper(target, idx+1)

    return helper(target, 0)


@time_execution
def count_construct_rec_memo(target: str, word_bank: list[str]) -> int:
    word_bank_len = len(word_bank)
    memo = {'': 1}
    memo_count = 0

    def helper(target: str, idx: int) -> int:
        nonlocal memo_count
        if target in memo:
            memo_count += 1
            return memo[target]
        if idx == word_bank_len:
            return 0

        if target.startswith(word_bank[idx]):
            memo[target] = helper(target.lstrip(word_bank[idx]), 0) + \
                helper(target, idx+1)
            return memo[target]
        else:
            return helper(target, idx+1)

    return f"{helper(target,0)}, memo_count: {memo_count}"
    return helper(target, 0)


@time_execution
def count_construct_rec_v2(target: str, word_bank: list[str]) -> int:
    def helper(target: str):
        if target == '':
            return 1

        total = 0
        for num in word_bank:
            if target.startswith(num):
                res = helper(target.lstrip(num))
                total += res

        return total

    return helper(target)


@time_execution
def count_construct_rec_v2_memo(target: str, word_bank: list[str]) -> int:
    memo = {'': 1}
    memo_count = 0

    def helper(target: str):
        nonlocal memo_count

        if target in memo:
            memo_count += 1
            return memo[target]

        total = 0
        for num in word_bank:
            if target.startswith(num):
                res = helper(target.lstrip(num))
                total += res

        memo[target] = total
        return total

    return f"{helper(target)}, memo_count: {memo_count}"
    return helper(target)


print(count_construct_rec("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct_rec_memo("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct_rec_v2("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct_rec_v2_memo("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct_tabulation("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
