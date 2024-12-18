import time
from utils import is_prime

N_A = 1000
N_B = 1000

t0 = time.time()
max_n = 0
ans = 0
for a in range(-N_A + 1, N_A):
    for b in range(2, N_B):
        n = 0
        while is_prime(n ** 2 + a * n + b):
            n += 1
        if n > max_n:
            max_n = n
            ans = a * b
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")