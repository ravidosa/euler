import time, itertools, math
import utils

N = 1000
M = [3, 5]

t0 = time.time()
ans = 0
for k in range(1, len(M) + 1):
    for subset in itertools.combinations(M, k):
        lcm = math.lcm(*subset)
        n = (N - 1) // lcm
        ans += (-1) ** (k + 1) * ((n + 1) * lcm * n // 2)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")