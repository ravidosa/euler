import time
from utils.sequences import pentagonal, pentagonal_under_index

N = 1000000

t0 = time.time()
partitions = {0: 1, 1: 1}
ans = 2
while True:
    partitions[ans] = sum(map(lambda p: (partitions.get(ans - pentagonal(p), 0) * (0 if p == 0 else -1 if p % 2 == 0 else 1)) % N, range(-pentagonal_under_index(ans), pentagonal_under_index(ans) + 1))) % N
    if partitions[ans] % N == 0:
        break
    ans += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")