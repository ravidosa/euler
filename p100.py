import time, math

N = 10 ** 12

t0 = time.time()
ans, discs = 15, 21
while discs <= N:
    ans, discs = 3 * ans + 2 * discs - 2, 4 * ans + 3 * discs - 3
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")