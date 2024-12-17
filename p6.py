import time

N = 100

t0 = time.time()
ans = (N * (N + 1) // 2) ** 2 - sum([i ** 2 for i in range(1, N + 1)])
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")