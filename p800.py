import time, math
from utils.primes import is_prime

E = 800800
B = 800800

t0 = time.time()
ans = 0
thresh = E * math.log10(B)
p = 2
while p * math.log10(p) <= 0.5 * thresh:
    if is_prime(p):
        low = p + 1
        high = thresh // math.log10(p)
        while low <= high:
            q = int((low + high) // 2)
            if p * math.log10(q) + q * math.log10(p) > thresh:
                high = q - 1
            else:
                low = q + 1
        while not is_prime(q):
            q += 1
        if p == 2:
            sieve = [1 for _ in range(q)]
            sieve[0:2] = [0] * 2
            for i in range(2, math.floor(math.sqrt(q)) + 1):
                if sieve[i] != 0:
                    sieve[2 * i:((q - 1) // i + 1) * i:i] = [0] * ((q - 1) // i - 1)
            primes = [i for i in range(q + 50) if is_prime(i)]
            prime_pi = [0] * (q + 1)
            prime_index = 0
            for i in range(1, q + 1):
                while True:
                    if primes[prime_index] > i:
                        prime_pi[i] = prime_index
                        break
                    prime_index += 1
        if p * math.log10(q) + q * math.log10(p) > thresh:
            ans += prime_pi[q] - prime_pi[p] - 1
        else:
            ans += prime_pi[q] - prime_pi[p]
    p += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")