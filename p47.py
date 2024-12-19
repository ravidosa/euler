import time, math
from utils.primes import prime_factorization

N = 4

t0 = time.time()
N_distinct = [False] * N
i = 2
while True:
    N_distinct[0:N - 1] = N_distinct[1:N]
    N_distinct[-1] = (len(prime_factorization(i)) == N)
    if all(N_distinct):
        ans = i - N + 1
        break
    i += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")