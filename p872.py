import time, math

N = 10 ** 17
K = 9 ** 17

t0 = time.time()
ans = N
steps = "{0:b}".format(N - K)
for i in range(len(steps)):
    if steps[i] == "0":
        continue
    ans += N - int(steps[i:], 2)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")