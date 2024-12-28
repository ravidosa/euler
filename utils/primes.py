import math, functools, itertools

prod = lambda x, y: x * y

def generate_n_primes(n):
    if n == 0:
        return []
    primes = [2]
    i = 3
    while len(primes) < n:
        if all([i % prime != 0 for prime in primes]):
            primes.append(i)
        i += 1
    return primes

def generate_primes_up_to(n):
    sieve = [i for i in range(n + 1)]
    sieve[1] = 0
    p = 2
    while p <= math.sqrt(n):
        if sieve[p] != 0:
            sieve[p * p:(n // p + 1) * p:p] = [0] * (n // p - p + 1)
        p += 1
    return [i for i in sieve if i != 0]

def is_prime(n):
    if n <= 1:
        return False
    for p in range(2, math.floor(math.sqrt(n)) + 1):
        if n % p == 0:
            return False
    return True

def next_prime(p):
    p += 1
    while not is_prime(p):
        p += 1
    return p

def prime_factorization(n):
    factor_dic = {}
    p = 2
    while p <= math.sqrt(n):
        if n % p == 0:
            n //= p
            factor_dic[p] = factor_dic.get(p, 0) + 1
        else:
            p += 1
    factor_dic[n] = factor_dic.get(n, 0) + 1
    return factor_dic

def num_divisors(n):
    factor_dic = prime_factorization(n)
    return functools.reduce(lambda x, y: x * (factor_dic[y] + 1), factor_dic, 1)

def divisors(n):
    factorization = prime_factorization(n)
    primes = list(factorization.keys())
    divisors = []
    exp = {factor: 0 for factor in factorization}
    finished = False
    while not finished:
        divisors.append(functools.reduce(prod, [factor ** exp[factor] for factor in factorization], 1))
        j = 0
        while True:
            exp[primes[j]] += 1
            if exp[primes[j]] <= factorization[primes[j]]:
                break
            exp[primes[j]] = 0
            j += 1
            if j >= len(primes):
                finished = True
                break
    return sorted(divisors)

def totient(n):
    factorization = prime_factorization(n)
    res = n
    for p in factorization:
        res -= res // p
    return res

def totient_up_to(n):
    sieve = [i for i in range(n + 1)]
    p = 2
    while p <= n:
        if sieve[p] == p:
            sieve[p::p] = [s - s // p for s in sieve[p::p]]
        p += 1
    return sieve

def primality_up_to(n):
    sieve = [True for _ in range(n + 1)]
    sieve[:2] = [False] * 2
    p = 2
    while p <= math.sqrt(n):
        if sieve[p] != 0:
            sieve[p * p:(n // p + 1) * p:p] = [False] * (n // p - p + 1)
        p += 1
    return sieve

def prime_pi_up_to(n):
    primality = primality_up_to(n)
    pp = [0] * (n + 1)
    p_index = 0
    for i in range(1, n + 1):
        pp[i] = p_index
        if primality[i]:
            p_index += 1
    return pp

def proper_divisors(n):
    return divisors(n)[:-1]

def is_perfect(n):
    return sum(proper_divisors(n)) == n

def is_abundant(n):
    return sum(proper_divisors(n)) > n

def is_deficient(n):
    return sum(proper_divisors(n)) < n

def num_squarefree_up_to(n):
    num_squarefree = n
    square_primes = list(map(lambda i: i ** 2, generate_primes_up_to(math.floor(math.sqrt(n)))))
    for intersection in range(1, len(square_primes) + 1):
        for subset in itertools.combinations(square_primes, intersection):
            a1 = math.lcm(*subset)
            m = n // a1
            num_squarefree -= (-1) ** (intersection + 1) * m
    return num_squarefree