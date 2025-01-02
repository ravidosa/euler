import time, math, itertools, functools
from utils.digits import digit_count

N = 12

t0 = time.time()
ans = 0
for sorted_digits in itertools.combinations_with_replacement("0123456789", N):
    n = int("".join(sorted_digits))
    dc = digit_count(n)
    perms = math.factorial(sum(dc)) // functools.reduce(lambda x, y: x * math.factorial(y), dc[1:], 1) * math.factorial(N - 1) // (math.factorial(N - sum(dc)) * math.factorial(sum(dc) - 1))
    ans += (perms - 1) * perms // 2
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")