import time
from utils.primes import is_prime
from utils.digits import generate_pandigital

t0 = time.time()
ans = 2
for n in [7, 4]:
    for pandigital in generate_pandigital(1, n):
        if is_prime(pandigital):
            ans = max(ans, pandigital)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")