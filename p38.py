import time
from utils.digits import is_pandigital

t0 = time.time()
ans = 0
for i in range(10 ** 5):
    concatenation = str(i)
    j = 2
    while len(concatenation) < 9:
        concatenation += str(i * j)
        j += 1
    concatenation = int(concatenation)
    if is_pandigital(1, 9, concatenation):
        ans = max(ans, concatenation)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")