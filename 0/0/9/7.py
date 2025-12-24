import time

t0 = time.time()
ans = (28433 * pow(2, 7830457, 10 ** 10) + 1) % (10 ** 10)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")