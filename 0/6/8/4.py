import time

N = 90
mod = 1000000007

t0 = time.time()
ans = 0
fib_n_1 = 0
fib_n = 1
ct = 2
while ct <= N:
    fib_n_1, fib_n = fib_n, fib_n_1 + fib_n
    q, r = fib_n // 9, fib_n % 9
    ss = (6 * (pow(10, q, mod) - 1) - 9 * q + pow(10, q, mod) * (r + 3) * r // 2 - r) % mod
    ans += ss
    ans %= mod
    ct += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")