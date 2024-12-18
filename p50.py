import time
from utils import is_prime

N = 1000000

t0 = time.time()
ans = 2
max_n = 0
ans = 0
p_1 = 2
while p_1 < N:
    prime_sum = 0
    if is_prime(p_1):
        prime_sum = p_1
        n = 1
        p_n = p_1 + 1
        while prime_sum < N:
            if is_prime(p_n):
                prime_sum += p_n
                n += 1
                if is_prime(prime_sum):
                    if n > max_n:
                        max_n = n
                        ans = prime_sum
            p_n += 1
    p_1 += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")