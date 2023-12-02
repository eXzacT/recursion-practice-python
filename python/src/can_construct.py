# Check if it's possible to create target string by using words from wordbank

from common import time_execution


@time_execution
def can_construct_rec(target: str, word_bank: list[str]) -> bool:
    def helper(target: str):
        if target == '':
            return True
        for word in word_bank:
            if target.startswith(word):
                if helper(target.lstrip(word)):
                    return True
        return False

    return helper(target)


@time_execution
def can_construct_rec_memo(target: str, word_bank: list[str]) -> bool:
    memo = {'': True}

    def helper(target: str):
        if target in memo:
            return memo[target]

        for word in word_bank:
            if target.startswith(word):
                if (res := helper(target.lstrip(word))):
                    memo[target] = res
                    return res

        memo[target] = False
        return False

    return helper(target)


@time_execution
def can_construct_rec_v2(target: str, word_bank: list[str]) -> bool:
    word_bank_len = len(word_bank)

    def helper(target: str, idx=0):
        if idx == word_bank_len:
            return False
        if target == '':
            return True

        if target.startswith(word_bank[idx]):
            return helper(target.lstrip(word_bank[idx]), 0) \
                or helper(target, idx+1)
        else:
            return helper(target, idx+1)

    return helper(target)


@time_execution
def can_construct_rec_v2_memo(target, word_bank):
    word_bank_len = len(word_bank)
    memo = {'': True}

    def helper(target, idx=0):
        if idx == word_bank_len:
            return False
        if target in memo:
            return memo[target]

        if target.startswith(word_bank[idx]):
            memo[target] = helper(target.lstrip(
                word_bank[idx]), 0) or helper(target, idx + 1)
            return memo[target]
        else:
            memo[target] = helper(target, idx + 1)
            return memo[target]

    return helper(target)


print(can_construct_rec("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(can_construct_rec_memo("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))

print(can_construct_rec_v2("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(can_construct_rec_v2_memo("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
