import time, math
from utils.geometry import herons

N = 1000000000

t0 = time.time()
ans = 0
s, area = 6, int(herons(6, 5, 5) * 4 / 6)
while 3 * s - 2 <= N:
    if s > 0:
        ans += 3 * s - 2
    s, area = -2 * s + -1 * area + 4, -3 * s + -2 * area + 4
s, area = 16, int(herons(16, 17, 17) * 4 / 16)
while 3 * s + 2 <= N:
    if s > 0:
        ans += 3 * s + 2
    s, area = -2 * s + -1 * area - 4, -3 * s + -2 * area - 4
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")