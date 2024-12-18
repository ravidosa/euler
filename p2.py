import time

N = 4000000

t0 = time.time()
ans = 2

a_n_1 = 1
a_n = 2

while a_n < N:
    a_n_1, a_n = a_n, a_n_1 + a_n
    if a_n % 2 == 0:
        ans += a_n
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")