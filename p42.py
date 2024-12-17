import time, math

words = open("words.txt", "r").read()
N = len(words)

t0 = time.time()
words = words[1:-1].split("\",\"")
values = [sum([ord(letter) - 64 for letter in word]) for word in words]
ans = sum([(-0.5 + math.sqrt(0.25 + 2 * value)).is_integer() for value in values])
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")