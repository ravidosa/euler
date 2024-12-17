import time, math

N = 1000000

def is_prime(i):
    if i <= 1:
        return False
    for p in range(2, math.floor(math.sqrt(i)) + 1):
        if i % p == 0:
            return False
    return True

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