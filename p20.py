import time, math
from utils.digits import sum_digits

N = 100

t0 = time.time()
fac = math.factorial(N)
for i in range(math.floor(math.log(N, 5))):
    fac //= (10 ** (N // (5 ** (i + 1))))
ans = sum_digits(fac)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")