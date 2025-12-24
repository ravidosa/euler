import time
from utils.primes import is_prime

N = 1000000

t0 = time.time()
ans = 0
for i in range(2, N):
    if is_prime(i):
        circular = True
        for j in range(1, len(str(i))):
            circ = int(str(i)[j:] + str(i)[:j])
            if not is_prime(circ):
                circular = False
                break
        if circular:
            ans += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")