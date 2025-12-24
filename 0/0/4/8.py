import time

N = 1000

t0 = time.time()
ans = sum(map(lambda i: pow(i, i, 10 ** 10), range(1, N + 1))) % (10 ** 10)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")