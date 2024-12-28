import time, math, itertools, functools
from utils.primes import generate_primes_up_to, prime_factorization

N = 1000000000
P = 120

t0 = time.time()
ans = 0
basis = {}
for m in generate_primes_up_to(P ** 2):
    fib_n_1 = 0
    fib_n = 1
    pi = 0
    while True:
        fib_n_1, fib_n = fib_n, (fib_n_1 + fib_n) % m
        pi += 1
        if (fib_n_1 == 0 and fib_n == 1) or pi > P:
            break
    if fib_n_1 == 0 and fib_n == 1 and P % pi == 0:
        basis[m] = pi
primes = list(basis.keys())
max_exp = list(map(lambda p: range(prime_factorization(P / basis[p]).get(p, 0) + 2), primes))
for combo in itertools.product(*max_exp):
    if math.lcm(*[basis[primes[i]] * primes[i] ** (combo[i] - 1) for i in range(len(primes)) if combo[i] != 0]) == P:
        if sum(map(lambda i: combo[i] * math.log(primes[i]), range(len(primes)))) < math.log(N):
            m = functools.reduce(lambda x, y: x * y, [primes[i] ** combo[i] for i in range(len(primes))], 1)
            ans += m
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")