import time
from utils.primes import generate_n_primes

N = 10001

t0 = time.time()
ans = generate_n_primes(N)[-1]
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")