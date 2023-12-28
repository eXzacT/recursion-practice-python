# Print N-bit binary numbers having more or equal 1s to 0s count
# Input : n = 4
# Output : '1111', '1110', '1101', '1100', '1011', '1010', '1001'

def binary_more_1s(n: int) -> list[str]:
    binary_nums = []
    max_zero_count = n//2

    def helper(s: str):
        if len(s) == 4:
            binary_nums.append(s)
            return

        helper(s+'1')
        if s.count('0') != max_zero_count:
            helper(s+'0')

    helper('1')
    return binary_nums


# Print N-bit binary numbers having more or equal 1s to 0s count in every prefix
# Input : n = 4
# Output : '1111', '1110', '1101', '1100', '1011', '1010'

def binary_more_1s_prefix(n: int) -> list[str]:
    binary_nums = []

    def helper(s: str):
        if len(s) == 4:
            binary_nums.append(s)
            return

        helper(s+'1')
        if s.count('1') > s.count('0'):
            helper(s+'0')

    helper('1')
    return binary_nums


print(binary_more_1s(4))
print(binary_more_1s_prefix(4))
