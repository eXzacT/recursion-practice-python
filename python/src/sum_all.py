def sum_all_memo(target, nums):
    memo = {}
    memo_hits = 0

    def helper(remainder, last_used=0):
        nonlocal memo_hits
        memo_key = (remainder, last_used)
        if memo_key in memo:
            memo_hits += 1
            return memo[memo_key]
        if remainder < 0 or last_used == len(nums):
            return None

        new_combs = []

        combs = helper(remainder - nums[last_used], last_used)
        if combs is not None:
            for comb in combs:
                new_combs.append(comb + [nums[last_used]])

        combs = helper(remainder, last_used + 1)
        if combs is not None:
            for comb in combs:
                new_combs.append(comb)

        memo[memo_key] = new_combs
        return new_combs

    result = helper(target)
    print(f"Memo hits: {memo_hits}")
    return result if result is not None else []


# Example usage
target = 5
nums = [1, 2, 3]
print(sum_all_memo(target, nums))
