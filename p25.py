import time, math

N = 1000

t0 = time.time()

fib_n_1 = 0
fib_n = 1
ans = 1

while math.log10(fib_n) + 1 < N:
    fib_n_1, fib_n = fib_n, fib_n_1 + fib_n
    ans += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")

t0 = time.time()
phi = (1 + math.sqrt(5)) / 2
ans = math.ceil((N - 1 + math.log10(5) / 2) / math.log10(phi))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")