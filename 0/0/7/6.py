import time
from utils.sequences import pentagonal, pentagonal_under_index

N = 100

t0 = time.time()
partitions = {0: 1, 1: 1}
for i in range(2, N + 1):
    partitions[i] = sum(map(lambda p: partitions.get(i - pentagonal(p), 0) * (-1 if p % 2 == 0 else 1), range(-pentagonal_under_index(i), pentagonal_under_index(i) + 1)))
ans = partitions[N] - 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")