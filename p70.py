import time
from utils.primes import totient_up_to
from utils.digits import is_permutations

N = 10000000

t0 = time.time()
min_totient_ratio = 2
ans = 2
totients = totient_up_to(N - 1)
for i in range(2, N):
    if i / totients[i] < min_totient_ratio and is_permutations([i, totients[i]]):
        min_totient_ratio = i / totients[i]
        ans = i
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")