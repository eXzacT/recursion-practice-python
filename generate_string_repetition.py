def generate_string_repetition(s: str, repetitions=10_000):
    s_repetition = ''.join([s for _ in range(repetitions)])
    return s_repetition
