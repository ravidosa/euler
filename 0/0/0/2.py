import time

N = 4000000

t0 = time.time()
ans = 2

fib_n_1 = 1
fib_n = 2

while fib_n < N:
    fib_n_1, fib_n = fib_n, fib_n_1 + fib_n
    if fib_n % 2 == 0:
        ans += fib_n
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")