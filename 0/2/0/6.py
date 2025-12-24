import time, math

t0 = time.time()
for i in range(int(math.sqrt(1020304050607080900) // 10) * 10, math.floor(math.sqrt(1929394959697989990)), 10):
    square = i ** 2
    if str(square)[::2] == "1234567890":
        ans = i
        break
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")