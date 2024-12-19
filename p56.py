import time, itertools
from utils.digits import sum_digits

N_A = 100
N_B = 100

t0 = time.time()
ans = max(map(lambda pair: sum_digits(pair[0] ** pair[1]), itertools.product(range(2, N_A), range(2, N_B))))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")