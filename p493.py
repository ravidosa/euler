import time, math

N = 10
K = 7
M = 20

t0 = time.time()
ans = K * (1 - math.comb(N * (K - 1), M) / math.comb(N * K, M))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")