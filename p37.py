import time
from utils.primes import is_prime
from utils.digits import odd_digits

t0 = time.time()
truncatable = []
i = 11
while len(truncatable) < 11:
    if odd_digits(i) or (str(i)[0] == "2" and odd_digits(int(str(i)[1:]))):
        if is_prime(i):
            if all([is_prime(int(str(i)[j:])) for j in range(1, len(str(i)))]) and all([is_prime(int(str(i)[:j])) for j in range(1, len(str(i)))]):
                truncatable.append(i)
    i += 1
ans = sum(truncatable)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")