import time, math, itertools, functools
from utils.digits import digit_count

N = 18
M = 1123455689

t0 = time.time()
ans = 0
for sorted_digits in itertools.combinations_with_replacement("0123456789", N):
    n = int("".join(sorted_digits))
    dc = digit_count(n)
    ans += (n * math.factorial(N) // functools.reduce(lambda x, y: x * math.factorial(y), dc, 1) // math.factorial(N - sum(dc))) % M
ans %= M
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")