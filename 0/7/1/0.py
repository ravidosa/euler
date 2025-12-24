import time

t0 = time.time()
pal = lambda i: pow(2, i // 2, 1000000)
twopal = [0, 1, 0, 2, 1, 4, 3, 9]
i = 9
while True:
    twopal = twopal[1:] + [(twopal[-2] + twopal[-4] + twopal[-8] + pal(i - 4) - pal(i - 8)) % 1000000]
    if twopal[-1] == 0:
        ans = i
        break
    i += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")