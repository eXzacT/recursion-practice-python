# Given two numbers num and pow, find ways num can be expressed as
# sum of n-th power of unique natural numbers.

def sum_of_powers(num: int, pow: int) -> list[int]:
    res = []

    def helper(start_num=1, acc=0, temp=[]):
        if acc == num:
            res.append(temp)
            return
        if acc > num or start_num > num:
            return

        helper(start_num+1, acc, temp)
        helper(start_num+1, acc + start_num**pow, temp + [start_num**pow])

    helper()
    return res


print(sum_of_powers(150, 2))
