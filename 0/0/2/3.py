import time, itertools
from utils.primes import is_abundant

N = 28124

t0 = time.time()
abundant = [i for i in range(2, N) if is_abundant(i)]
abundant_sums = set([x + y for x, y in itertools.combinations_with_replacement(abundant, 2) if x + y < N])
ans = (N - 1) * N // 2 - sum(abundant_sums)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")