import time, math
from utils.primes import is_prime, next_prime, prime_pi_up_to

E = 800800
B = 800800

t0 = time.time()
ans = 0
thresh = E * math.log10(B)
p = 2
while p * math.log10(p) <= 0.5 * thresh:
    low = next_prime(p)
    high = thresh // math.log10(p)
    while low <= high:
        q = int((low + high) // 2)
        if p * math.log10(q) + q * math.log10(p) > thresh:
            high = q - 1
        else:
            low = q + 1
    if not is_prime(q):
        q = next_prime(q)
    if p == 2:
        pp = prime_pi_up_to(next_prime(q))
    if p * math.log10(q) + q * math.log10(p) > thresh:
        ans += pp[q] - pp[p] - 1
    else:
        ans += pp[q] - pp[p]
    p = next_prime(p)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")