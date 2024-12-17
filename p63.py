import time, math

t0 = time.time()
powers = set()
for i in range(1, 10):
    for n in range(1, max(2, math.ceil(1 / (1 - math.log10(i))))):
        if n == len(str(i ** n)):
            powers.add(i ** n)
ans = len(powers)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")