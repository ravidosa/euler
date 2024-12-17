import time

t0 = time.time()
products = set()
for x in range(10, 100):
    for y in range(100, 1000):
        if "".join(sorted(str(x) + str(y) + str(x * y))) == "123456789":
            products.add(x * y)
for x in range(1, 10):
    for y in range(1000, 10000):
        if "".join(sorted(str(x) + str(y) + str(x * y))) == "123456789":
            products.add(x * y)
ans = sum(products)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")