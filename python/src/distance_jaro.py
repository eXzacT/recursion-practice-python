'''What's the minimum number of substitutions to make word1 same as word2 if both words are of same length
    Also known as Jaro distance
    Not a recursive problem but I implemented other string distances and wanted to try this one too
'''
from common import time_execution


@time_execution()
def jaro_distance(word1: str, word2: str) -> float:
    if word1 == word2:
        return 1.0

    l1, l2 = len(word1), len(word2)
    if l1 == 0 or l2 == 0:
        return 0.0

    max_dist = int(max(l1, l2) / 2) - 1
    match1 = [False] * l1
    match2 = [False] * l2
    m = 0

    # Find matching characters
    for i in range(l1):
        start = max(0, i - max_dist)
        end = min(i + max_dist + 1, l2)

        for j in range(start, end):
            # Only consider characters we didn't match before
            if not match2[j] and word1[i] == word2[j]:
                match1[i] = match2[j] = True
                m += 1
                break

    if m == 0:
        return 0.0

    # Count transpositions(meaning if we swapped those 2 chars in word1, would they now match word2)
    k = t = 0
    for i in range(l1):
        if match1[i]:
            while not match2[k]:
                k += 1
            if word1[i] != word2[k]:
                t += 1
            k += 1

    # Divided by 2 to ignore the permutation
    t /= 2

    # Step 3: Calculate Jaro distance
    return (1/3) * (m / l1 + m / l2 + (m - t) / m)


print(jaro_distance("FAREMVIEL", "FARMVILLE"))
