import time

N = 100

t0 = time.time()
ans = (N * (N + 1) // 2) ** 2 - N * (N + 1) * (2 * N + 1) // 6
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")