import time
from utils.primes import totient

N = 1000000

t0 = time.time()
max_totient_ratio = 2
ans = 2
for i in range(2, N + 1):
    totient_ratio = i / totient(i)
    if totient_ratio > max_totient_ratio:
        max_totient_ratio = totient_ratio
        ans = i
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")