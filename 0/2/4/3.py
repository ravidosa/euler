import time
from utils.primes import totient, next_prime

threshold = 15499 / 94744

t0 = time.time()
prime_prod = 2
p = 2
found = False
while not found:
    resilience = totient(prime_prod) / (prime_prod - 1)
    if resilience < threshold:
        prime_prod //= p
        for i in range(1, p):
            ans = i * prime_prod
            resilience = totient(ans) / (ans - 1)
            if resilience < threshold:
                print(threshold, resilience)
                found = True
                break
    p = next_prime(p)
    prime_prod *= p
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")