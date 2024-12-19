import time

names = open("names.txt", "r").read()
N = len(names)

t0 = time.time()
names = sorted(names[1:-1].split("\",\""))
ans = sum(map(lambda pair: (pair[0] + 1) * sum(map(lambda letter: ord(letter) - 64, pair[1])), enumerate(names)))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")