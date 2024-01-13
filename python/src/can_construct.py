# Check if it's possible to create target string by using words from wordbank

from common import time_execution


@time_execution()
def can_construct_tabulation(target: str, word_bank: list[str]) -> bool:
    target_len = len(target)
    table = [None for _ in range(target_len+1)]
    table[0] = ''
    for idx in range(target_len+1):
        if table[idx] is not None:
            for word in word_bank:
                new_word = table[idx]+word
                if new_word == target:
                    return True
                # No point adding new words that don't match target
                if not target.startswith(new_word):
                    continue

                table[len(new_word)] = new_word

    return False


@time_execution()
def can_construct_tabulation_v2(target: str, word_bank: list[str]) -> bool:
    target_len = len(target)
    table = [False for _ in range(target_len+1)]
    table[0] = True
    for idx in range(target_len+1):
        if table[idx]:
            for word in word_bank:
                if word == target[idx:idx+len(word)]:
                    table[idx+len(word)] = True

    return table[-1]


@time_execution()
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


@time_execution()
def can_construct_rec_memo(target: str, word_bank: list[str]) -> bool:
    memo = {'': True}
    memo_count = 0

    def helper(target: str):
        nonlocal memo_count

        if target in memo:
            memo_count += 1
            return memo[target]

        for word in word_bank:
            if target.startswith(word):
                if (res := helper(target.lstrip(word))):
                    memo[target] = res
                    return res

        memo[target] = False
        return False

    return f"{helper(target)}, memo_count {memo_count}"


@time_execution()
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


@time_execution()
def can_construct_rec_v2_memo(target, word_bank):
    word_bank_len = len(word_bank)
    memo = {'': True}
    memo_count = 0

    def helper(target, idx=0):
        nonlocal memo_count

        if idx == word_bank_len:
            return False
        if target in memo:
            memo_count += 1
            return memo[target]

        if target.startswith(word_bank[idx]):
            memo[target] = helper(target.lstrip(
                word_bank[idx]), 0) or helper(target, idx + 1)
            return memo[target]
        else:
            memo[target] = helper(target, idx + 1)
            return memo[target]

    return f"{helper(target)}, memo_count {memo_count}"
    return helper(target)


print(can_construct_tabulation("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(can_construct_tabulation_v2("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))

print(can_construct_rec("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(can_construct_rec_memo("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))

print(can_construct_rec_v2("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(can_construct_rec_v2_memo("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))

print(can_construct_rec_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
      "e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeee"]))
print(can_construct_rec_v2_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
      "e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeee"]))
