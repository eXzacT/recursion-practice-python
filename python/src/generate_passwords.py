# Generate all passwords from given character set
import itertools


def generate_passwords(char_set: set[str]):
    passwords = ['']
    for char in char_set:
        new_passwords = [p[:i] + char + p[i:]
                         for p in passwords
                         for i in range(len(p) + 1)
                         if char not in p]
        passwords += new_passwords
    return passwords[1:]


def generate_passwords_rec(char_set: set[str]):
    set_len = len(char_set)

    def helper(prefix='', remaining=char_set):
        if len(prefix) == set_len:
            return []

        permutations = [prefix + char for char in remaining]

        for char in remaining:
            new_remaining = remaining - {char}
            permutations += helper(prefix + char, new_remaining)
        return permutations

    return helper()


print(generate_passwords({'a', 'b', 'd'}))
print(generate_passwords_rec({'a', 'b', 'd'}))

# Bonus


def generate_passwords_itertools(char_set: set[str]):
    passwords = []

    for size in range(1, len(char_set)+1):
        for permutations in itertools.permutations(char_set, size):
            passwords.append(''.join(permutations))

    return passwords


print(generate_passwords_itertools({'a', 'b', 'd'}))
