import time
from utils.primes import is_prime
from utils.digits import is_permutations

t0 = time.time()
for a_1 in range(1000, 100000):
    found = False
    for d in range(2, (10000 - a_1) // 2, 2):
        a_2 = a_1 + d
        a_3 = a_1 + 2 * d
        if is_permutations([a_1, a_2, a_3]):
            if a_1 != 1487 and is_prime(a_1) and is_prime(a_2) and is_prime(a_3):
                ans = str(a_1) + str(a_2) + str(a_3)
                found = True
                break
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")