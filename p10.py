import time
from utils.primes import generate_primes_up_to_n

N = 2000000

t0 = time.time()
ans = sum(generate_primes_up_to_n(N - 1))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")