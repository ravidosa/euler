import time
from utils.primes import primality_up_to
from utils.digits import digit_count

N = 8

t0 = time.time()
max_check = 10 ** 7
primes = primality_up_to(max_check)
for p in range(max_check):
    if primes[p]:
        dc = digit_count(p)
        if max(dc) == 3:
            replace_digit = dc.index(3)
            if sum(map(lambda i: primes[int(str(p).replace(str(replace_digit), str(i)))] and str(p).replace(str(replace_digit), str(i))[0] != "0", range(10))) == N:
                break
ans = p
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")