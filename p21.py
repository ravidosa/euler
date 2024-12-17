import time, math, functools

N = 10000

t0 = time.time()
amicable = set()
proper_divisors_dic = {1: 0}
for i in range(2, N):
    if i not in proper_divisors_dic:
        path = [i]
        while path[-1] not in proper_divisors_dic and 1 < path[-1] < N:

            curr = path[-1]
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
            proper_divisors_dic[path[-1]] = sum(divisors) - path[-1]
            path.append(sum(divisors) - path[-1])
            
        if len(path) >= 3 and path[-1] == path[-3]:
            amicable.add(path[-1])
            amicable.add(path[-2])
ans = sum(amicable)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")