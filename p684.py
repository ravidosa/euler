import time

N = 90
mod = 1000000007

t0 = time.time()
ans = 0
a_n_1 = 0
a_n = 1
ct = 2
while ct <= N:
    a_n_1, a_n = a_n, a_n_1 + a_n
    q, r = a_n // 9, a_n % 9
    ss = (6 * (pow(10, q, mod) - 1) - 9 * q + pow(10, q, mod) * (r + 3) * r // 2 - r) % mod
    ans += ss
    ans %= mod
    ct += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")