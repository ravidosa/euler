import time, math

N = 100
M = 1000000

t0 = time.time()
ans = sum([math.comb(n, r) > M for n in range(1, N + 1) for r in range(n + 1)])
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")