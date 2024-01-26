'''What's the minimum number of substitutions to go from word1 to word2 if both words are of same length
    Also known as Hamming distance
'''
from common import time_execution


@time_execution()
def hamming_distance_iter(word1: str, word2: str) -> int:
    return sum(word1[i] != word2[i] for i in range(len(word1)))


@time_execution()
def hamming_distance_rec(word1: str, word2: str) -> int:
    def helper(i: int) -> int:
        # Same length so doesn't matter which word
        if i == len(word1):
            return 0
        if word1[i] == word2[i]:
            return helper(i+1)
        return 1+helper(i+1)

    return helper(0)


word1 = "karolin"
word2 = "kathrin"

print(hamming_distance_iter(word1, word2))
print(hamming_distance_rec(word1, word2))
