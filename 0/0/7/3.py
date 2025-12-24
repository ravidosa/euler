import time, math

N = 12000
n1, d1 = 1, 3
n2, d2 = 1, 2

t0 = time.time()
ans = 0
for d in range(2, N + 1):
    for n in range(math.ceil(d * n1 / d1), math.ceil(d * n2 / d2)):
        if math.gcd(n, d) != 1:
            continue
        if n1 / d1 < n / d and n / d < n2 / d2:
            ans += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")