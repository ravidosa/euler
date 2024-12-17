import time

N = 1000

t0 = time.time()
ans = sum([pow(i, i, 10 ** 10) for i in range(1, N + 1)]) % (10 ** 10)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")