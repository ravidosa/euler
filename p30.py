import time, math, scipy
from utils.digits import sum_digits

N = 5

t0 = time.time()
n = math.floor(-(scipy.special.lambertw(-9 ** (-N) * math.log(10) / 10, -1).real) / math.log(10))
ans = sum(map(lambda i: i if i == sum_digits(i, lambda x: x ** 5) else 0,  range(2, 10 ** n)))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")