import time, math

N = 1000

t0 = time.time()
for a in range(1, N // 2):
    if (N ** 2 // 2) % (a - N) == 0:
        break
b = (N ** 2 // 2) // (a - N) + N
c = int(math.sqrt(a ** 2 + b ** 2))
ans = a * b * c
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")