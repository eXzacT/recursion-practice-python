# Return how to construct a target string using words from a list of strings
from common import time_execution


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

    def helper(target: str, idx: int) -> int:
        if target in memo:
            return memo[target]
        if idx == word_bank_len:
            return 0

        if target.startswith(word_bank[idx]):
            memo[target] = helper(target.lstrip(word_bank[idx]), 0) + \
                helper(target, idx+1)
            return memo[target]
        else:
            return helper(target, idx+1)

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

    def helper(target: str):
        if target in memo:
            return memo[target]

        total = 0
        for num in word_bank:
            if target.startswith(num):
                res = helper(target.lstrip(num))
                total += res

        memo[target] = total
        return total

    return helper(target)


print(count_construct_rec("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct_rec("purple", [
      "purp", "p", "ur", "le", "purpl"]))

print(count_construct_rec_memo("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct_rec_memo("purple", [
      "purp", "p", "ur", "le", "purpl"]))

print(count_construct_rec_v2("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct_rec_v2("purple", [
      "purp", "p", "ur", "le", "purpl"]))

print(count_construct_rec_v2_memo("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct_rec_v2_memo("purple", [
      "purp", "p", "ur", "le", "purpl"]))
