import time, math

t0 = time.time()
i = 2
while True:
    found = False
    for j in range(1, i):
        p_i = i * (3 * i - 1) // 2
        p_j = j * (3 * j - 1) // 2
        if ((1 + math.sqrt(1 + 24 * (p_i + p_j))) / 6).is_integer() and ((1 + math.sqrt(1 + 24 * (p_i - p_j))) / 6).is_integer():
            ans = p_i - p_j
            found = True
            break
    if found:
        break
    i += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")