import time
from utils.primes import totient_up_to

N = 1000000

t0 = time.time()
ans = sum(totient_up_to(N)[2:])
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")