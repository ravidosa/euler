import time, math

N = 20

t0 = time.time()
ans = math.lcm(*(i for i in range(1, N + 1)))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")