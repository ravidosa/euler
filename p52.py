import time
from utils.digits import is_permutations

t0 = time.time()
ans = 1
while True:
    if is_permutations([ans * j for j in range(1, 7)]):
        break
    ans += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")