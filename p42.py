import time, math
from utils.sequences import is_triangular

words = open("words.txt", "r").read()
N = len(words)

t0 = time.time()
words = words[1:-1].split("\",\"")
ans = sum(map(lambda word: is_triangular(sum(map(lambda letter: ord(letter) - 64, word))), words))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")