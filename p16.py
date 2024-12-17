import time

N = 1000
B = 2

t0 = time.time()
ans = 0
exp = B ** N
while exp > 0:
    ans += (exp % 10)
    exp //= 10
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")