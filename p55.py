import time

N = 10000
M = 50

t0 = time.time()
ans = 0
for i in range(1, N):
    curr = i
    ct = 0
    while (curr == i or str(curr) != str(curr)[::-1]) and ct < M:
        ct += 1
        curr = curr + int(str(curr)[::-1])
    if ct == M:
        ans += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")