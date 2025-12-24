import time, math
from utils.digits import square_root_digits, sum_digits

N = 100
prec = 100

t0 = time.time()
ans = sum(map(lambda i: sum(square_root_digits(i, prec - len(str(math.floor(math.sqrt(i)))))) if not math.sqrt(i).is_integer() else 0, range(1, N + 1)))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")