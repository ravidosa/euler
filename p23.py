import time, math, itertools, functools

N = 28124

t0 = time.time()
abundant = set()
for i in range(2, N):
    curr = i
    factor_dic = {}
    p = 2
    while p <= math.sqrt(curr):
        if curr % p == 0:
            curr //= p
            factor_dic[p] = factor_dic.get(p, 0) + 1
        else:
            p += 1
    factor_dic[curr] = factor_dic.get(curr, 0) + 1

    primes = list(factor_dic.keys())
    divisors = []
    num_factors = len(factor_dic)
    exp = {factor: 0 for factor in factor_dic}
    finished = False
    while not finished:
        divisors.append(functools.reduce(lambda x, y: x * y, [factor ** exp[factor] for factor in factor_dic], 1))
        j = 0
        while True:
            exp[primes[j]] += 1
            if exp[primes[j]] <= factor_dic[primes[j]]:
                break
            exp[primes[j]] = 0
            j += 1
            if j >= num_factors:
                finished = True
                break
    if sum(divisors) - i > i:
        abundant.add(i)
abundant_sums = set([x + y for x, y in itertools.combinations_with_replacement(abundant, 2) if x + y < N])
ans = (N - 1) * N // 2 - sum(abundant_sums)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")