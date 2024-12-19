import time
from utils.primes import is_prime
from utils.cryptography import baby_step_giant_step

N = 1000

t0 = time.time()
max_period = 0
ans = 2

for d in range(2, N):
    if is_prime(d) and d not in [2, 5]:
        order_10 = baby_step_giant_step(10, 1, d)
        if order_10 > max_period:
            max_period = order_10
            ans = d
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")