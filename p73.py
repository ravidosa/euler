import time

N = 8
n1, d1 = 1, 3
n2, d2 = 1, 2

t0 = time.time()
ans = 0
for d in range(2, N + 1):
    for n in range(1, d):
        if n1 / d1 < n / d and n / d < n2 / d2:
            ans += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")