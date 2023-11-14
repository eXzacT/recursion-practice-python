# Partition given string in a fibonacci sequence manner

def split_into_fibonacci(s: str) -> bool:
    for x_len in range(1, len(s)):
        for y_len in range(1, len(s) - x_len):
            if split_into_fibonacci_helper(s, x_len, y_len):
                return True
    print("Not a fibonacci-like sequence")
    return False


def split_into_fibonacci_helper(s: str, x_len: int, y_len: int) -> bool:
    x = int(s[:x_len])
    y = int(s[x_len:x_len + y_len])
    idx = x_len + y_len

    # If x and y are not part of a sequence we are returning False anyway
    seq = [x, y]

    while idx < len(s):
        z = x + y
        z_str = str(z)
        z_len = len(z_str)

        # Check if x and y have their sum as the next number in the string
        if not s.startswith(z_str, idx):
            return False

        # Add their sum to the sequence(we already added x and y outside the loop)
        seq.append(z)

        x, y = y, z
        idx += z_len

    # We only get here if the entire string is a valid sequence
    print(' '.join(map(str, seq)))

    return True


def split_into_fibonacci_rec(s: str) -> None:
    seq = []
    stripped_s = s.lstrip('0')
    # Preserve 1 leading 0 if there was any otherwise keep same string
    s = '0'+stripped_s if len(stripped_s) < len(s) else s
    if split_into_fibonacci_helper_rec(s, seq):
        if len(seq) >= 3:
            print(' '.join(map(str, seq)))
        else:
            print("Not a fibonacci-like sequence")
    else:
        print("Not a fibonacci-like sequence")


def split_into_fibonacci_helper_rec(s: str, seq: list, idx=0) -> bool:
    # Base case
    if idx == len(s) and len(seq) >= 3:
        return True
    curr = 0
    for i in range(idx, len(s)):
        # Pull the number from the string, first 1 digit, then 2, 3 etc..
        curr = curr * 10 + int(s[i])
        if curr > 2**31 - 1:
            break
        if s[idx] == '0' and i > idx:
            break
        # Example 10>9, we can only turn 10 into a 3 digit number next loop
        # Any three-digit number '10X' is clearly > than 9
        if len(seq) > 2 and curr > seq[-1]+seq[-2]:
            break
        if len(seq) < 2 or curr == seq[-1]+seq[-2]:
            seq.append(curr)
            if split_into_fibonacci_helper_rec(s, seq, i + 1):
                return True
            # Kicking last added seq because it wasn't fibonacci-like
            seq.pop()

    return False


split_into_fibonacci_rec('50551015')
split_into_fibonacci('11235813')
split_into_fibonacci('3547821136')
split_into_fibonacci_rec('11235813')
split_into_fibonacci_rec('3547821136')
split_into_fibonacci_rec('0000011')
split_into_fibonacci('0000011')
split_into_fibonacci_rec('57158')
split_into_fibonacci('57158')
split_into_fibonacci_rec('5710')
split_into_fibonacci('5710')
