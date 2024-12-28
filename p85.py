import time, math

N = 2000000

t0 = time.time()
mind = N
ans = 0
for i in range(1, math.floor((-1 + math.sqrt(1 + 8 * N)) / 2)):
    for j in range(1, i + 1):
        squares = i * (i + 1) * j * (j + 1) // 4
        if abs(squares - N) < mind:
            mind = abs(squares - N)
            ans = i * j
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")