import time
from utils.primes import is_prime

threshold = 0.1

t0 = time.time()
ans = 1
prime_ratio = 1
spiral_primes = 0
while prime_ratio >= threshold:
    ans += 2
    steps = ans // 2 + 1
    if is_prime(4 * steps ** 2 - 10 * steps + 7):
        spiral_primes += 1
    if is_prime(4 * steps ** 2 - 8 * steps + 5):
        spiral_primes += 1
    if is_prime(4 * steps ** 2 - 6 * steps + 3):
        spiral_primes += 1
    prime_ratio = spiral_primes / (4 * steps - 3)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")