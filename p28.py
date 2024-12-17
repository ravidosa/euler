import time

N = 1001

t0 = time.time()
steps = N // 2 + 1
ans = -3
ans += 4 * (4 * steps * (steps + 1) * (2 * steps + 1) // 6)
ans -= 4 * (7 * steps * (steps + 1) // 2)
ans += 4 * (4 * steps)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")