from common import time_execution


@time_execution()
def binary_max_2_zeros(n: int) -> list[str]:
    bins = []

    def helper(chars: list[str]) -> None:
        if len(chars) == n:
            bins.append(''.join(chars))
            return
        for digit in ['0', '1']:
            chars.append(digit)
            helper(chars)
            chars.pop()

    helper([])
    return list(filter(lambda s: s.count('0') <= 2, bins))


@time_execution()
def binary_max_2_zeros_v2(n: int) -> list[str]:
    bins = []

    def helper(s: str) -> None:
        if len(s) == n:
            bins.append(s)
            return
        helper(s+"0")
        helper(s+"1")

    helper("")
    return list(filter(lambda s: s.count('0') <= 2, bins))


@time_execution()
def binary_max_2_zeros_v3(n: int) -> list[str]:
    bins = []

    def helper(s: str) -> None:
        if len(s) == n:
            bins.append(s)
            return
        if s.count("0") < 2:
            helper(s+"0")
        helper(s+"1")

    helper("")
    return bins


@time_execution()
def binary_max_2_zeros_v4(n: int) -> list[str]:
    def helper(n: int):
        if n == 0:
            return ['']

        from_next = helper(n-1)
        bins = []
        for b in from_next:
            if b.count("0") < 2:
                bins.append(b+"0")
            bins.append(b+"1")

        return bins

    return helper(n)


print(binary_max_2_zeros(4))
print(binary_max_2_zeros_v2(4))
print(binary_max_2_zeros_v3(4))
print(binary_max_2_zeros_v4(4))
