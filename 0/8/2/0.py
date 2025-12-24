import time
from utils.primes import generate_primes_up_to

N = 7

t0 = time.time()
ans = 0

t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")