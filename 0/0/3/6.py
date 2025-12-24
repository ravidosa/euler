import time

N = 1000000

t0 = time.time()
ans = 0
for i in range(1, N):
    decimal = str(i)
    binary = "{0:b}".format(i)
    if decimal == decimal[::-1] and binary == binary[::-1]:
        ans += i
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")