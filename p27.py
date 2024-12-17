import time, math

N_A = 1000
N_B = 1000

def is_prime(i):
    if i <= 1:
        return False
    for p in range(2, math.floor(math.sqrt(i)) + 1):
        if i % p == 0:
            return False
    return True

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