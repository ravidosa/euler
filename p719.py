import time, math
from utils.digits import decimal_partition

N = 10 ** 12

t0 = time.time()
ans = 0
for i in range(0, math.floor(math.sqrt(N)) + 1, 9):
    square = i ** 2
    for partition in decimal_partition(square):
        if sum(partition) == i and len(partition) > 1:
            ans += square
            break
    i_ = i + 1
    if i_ ** 2 <= N:
        square = i_ ** 2
        for partition in decimal_partition(square):
            if sum(partition) == i_ and len(partition) > 1:
                ans += square
                break
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")