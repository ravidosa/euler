import time, math

N = 100
M = 1000000

t0 = time.time()
ans = sum(map(lambda n: sum(map(lambda r: (1 if r == (n + 1) // 2 and n % 2 == 0 else 2) * (math.comb(n, r) > M), range((n + 1) // 2, n + 1))), range(1, N + 1)))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")