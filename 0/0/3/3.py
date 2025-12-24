import time, math

t0 = time.time()
n, d = 1, 1
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if (a != b or b != c) and (10 * a + b) * c == (10 * b + c) * a:
                n *= a
                d *= c
ans = d // math.gcd(n, d)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")