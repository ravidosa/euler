import time
from utils.digits import sum_digits

N = 1000
B = 2

t0 = time.time()
ans = sum_digits(B ** N)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")