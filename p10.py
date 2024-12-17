import time

N = 2000000

t0 = time.time()
sieve = [i for i in range(2, N)]
i = 2
while i <= N - 2:
    if sieve[i - 2] != 0:
        sieve[2 * i - 2:((N - 1) // i + 1) * i - 2:i] = [0] * ((N - 1) // i - 1)
    i += 1
ans = sum(sieve)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")