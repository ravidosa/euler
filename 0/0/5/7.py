import time

N = 1000

t0 = time.time()
ans = 0

d_n_1 = 0
d_n = 1

for _ in range(N - 1):
    d_n_1, d_n = d_n, d_n_1 + 2 * d_n
    n_n = d_n + d_n_1
    if len(str(n_n)) > len(str(d_n)):
        ans += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")