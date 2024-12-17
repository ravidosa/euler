import time

N = 10001

t0 = time.time()
primes = [2]
i = 3
while len(primes) < N:
    if all([i % prime != 0 for prime in primes]):
        primes.append(i)
    i += 1
ans = primes[-1]
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")