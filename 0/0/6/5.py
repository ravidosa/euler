import time
from utils.digits import sum_digits

N = 100

t0 = time.time()
cont_fraction = [2] + [1 if i % 3 != 1 else 2 * (i + 2) // 3 for i in range(N - 1)]
n, d = 1, cont_fraction[-1]
for i in range(N - 2, -1, -1):
    n, d = d, cont_fraction[i] * d + n
n, d = d, n
ans = sum_digits(n)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")