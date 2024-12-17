import time

N = open("names.txt", "r").read()

t0 = time.time()
names = sorted(N[1:-1].split("\",\""))
ans = sum([(i + 1) * sum([ord(letter) - 64 for letter in names[i]]) for i in range(len(names))])
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")