import time

N = 1000
B = 2

t0 = time.time()
ans = 0
pow = B ** N
while pow > 0:
    ans += (pow % 10)
    pow //= 10
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")