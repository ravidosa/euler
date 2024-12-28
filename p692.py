import time

N = 23416728348467685

t0 = time.time()
fib_n_2 = 1
fib_n_1 = 1
fib_n = 2
g_n_2 = 1
g_n_1 = 1
g_n = 3

while fib_n != N:
    fib_n_2, fib_n_1, fib_n = fib_n_1, fib_n, fib_n_1 + fib_n
    g_n_2, g_n_1, g_n = g_n_1, g_n, g_n + g_n_1 + fib_n - fib_n_2
ans = g_n
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")