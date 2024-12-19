import time, math
from utils.sequences import hexagonal, is_pentagonal

t0 = time.time()
i = 144
while True:
    h_i = hexagonal(i)
    if is_pentagonal(h_i):
        ans = h_i
        break
    i += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")