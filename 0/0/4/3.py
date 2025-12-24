import time
from utils.digits import generate_pandigital

t0 = time.time()
ans = 0
primes = [2, 3, 5, 7, 11, 13, 17]
for pandigital in generate_pandigital(0, 9):
    if all([int(str(pandigital).zfill(10)[i + 1:i + 4]) % primes[i] == 0 for i in range(7)]):
        ans += pandigital
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")