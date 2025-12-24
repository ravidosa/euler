import time, math

N = 20
M = 20

t0 = time.time()
ans = math.comb(N + M, N)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")