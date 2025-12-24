import time, math
from utils.sequences import pentagonal, is_pentagonal

t0 = time.time()
i = 2
while True:
    found = False
    for j in range(1, i):
        p_i = pentagonal(i)
        p_j = pentagonal(j)
        if is_pentagonal(p_i + p_j) and is_pentagonal(p_i - p_j):
            ans = p_i - p_j
            found = True
            break
    if found:
        break
    i += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")