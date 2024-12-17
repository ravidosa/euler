import time, math

t0 = time.time()
i = 144
while True:
    h_i = i * (2 * i - 1)
    if ((1 + math.sqrt(1 + 24 * h_i)) / 6).is_integer():
        ans = h_i
        break
    i += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")