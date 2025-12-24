import time, math
from utils.digits import sum_digits, square_root_digits

N = 1000
K = 13

t0 = time.time()
ans = sum(square_root_digits(K, N)) - sum_digits(math.floor(math.sqrt(K)))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")