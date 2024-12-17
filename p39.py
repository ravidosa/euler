import time

N = 1000

t0 = time.time()
max_sols = 0
ans = 0
for p in range(12, N + 1, 2):
    sols = 0
    for a in range(1, p // 2):
        if (p ** 2 // 2) % (a - p) == 0:
            sols += 1
    if sols > max_sols:
        max_sols = sols
        ans = p
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")