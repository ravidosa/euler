import time
from utils.digits import is_pandigital

t0 = time.time()
products = set()
for x in range(10, 100):
    for y in range(100, 1000):
        if is_pandigital(1, 9, int(str(x) + str(y) + str(x * y))):
            products.add(x * y)
for x in range(1, 10):
    for y in range(1000, 10000):
        if is_pandigital(1, 9, int(str(x) + str(y) + str(x * y))):
            products.add(x * y)
ans = sum(products)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")