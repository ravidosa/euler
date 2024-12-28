import time
from utils.primes import is_prime, generate_primes_up_to

N_A = 1000
N_B = 1000

t0 = time.time()
max_n = 0
ans = 0
b_candidates = generate_primes_up_to(N_B)
for b in b_candidates:
    for a in range(-b + 2, N_A, 2):
        n = 0
        while is_prime(n ** 2 + a * n + b):
            n += 1
        if n > max_n:
            max_n = n
            ans = a * b
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")