import time, math
from utils.primes import prime_factorization

N = 10 ** 8

t0 = time.time()
ans = 0
for i in range(2, N + 1):
    if i % 10000 == 0:
        print(i)
    factorization = prime_factorization(i)
    m = 1
    for factor in factorization:
        e = factorization[factor]
        while sum(map(lambda j: e // factor ** j, range(factorization[factor] + 1))) >= factorization[factor]:
            e -= 1
        if sum(map(lambda j: e // factor ** j, range(factorization[factor] + 1))) < factorization[factor]:
            e += 1
        m = max(m, factor * e)
    ans += m
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")