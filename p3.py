import time, math
N = 600851475143

t0 = time.time()
ans = N
p = 2

while p <= math.sqrt(ans):
    if ans % p == 0:
        ans //= p
    else:
        p += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")