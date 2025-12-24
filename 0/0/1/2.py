import time, math
from utils.primes import num_divisors
from utils.sequences import triangular

N = 500

t0 = time.time()
max_divisors = 0
i = int((N + 1) // math.sqrt(2))
while max_divisors < N:
    tri_i = triangular(i)
    num_divisors_tri_i = num_divisors(tri_i)
    if num_divisors_tri_i > max_divisors:
        max_divisors = num_divisors_tri_i
        ans = tri_i
    i += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")