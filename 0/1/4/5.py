import time
from utils.digits import reverse, all_odd

N = 10 ** 9

t0 = time.time()
ans = sum(all_odd(i + reverse(i)) for i in range(1, N) if i % 10 != 0)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")