import time, math

N = 1000000
n = 3
d = 7

t0 = time.time()
best_left_approx = 0
ans = 0
for i in range(2, N + 1):
    if i % d != 0:
        if math.floor(n / d * i) / i > best_left_approx:
            best_left_approx = math.floor(n / d * i) / i
            ans = math.floor(n / d * i)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")