import time, math, functools

N = 10000

t0 = time.time()
amicable = set()
proper_divisors_dic = {1: 0}
for i in range(2, N):
    if i not in proper_divisors_dic:
        path = [i]
        while path[-1] not in proper_divisors_dic and 1 < path[-1] < N:

            temp = path[-1]
            factor_dic = {}
            p = 2
            while p <= math.sqrt(temp):
                if temp % p == 0:
                    temp //= p
                    factor_dic[p] = factor_dic.get(p, 0) + 1
                else:
                    p += 1
            factor_dic[temp] = factor_dic.get(temp, 0) + 1

            primes = list(factor_dic.keys())
            proper_divisors = []
            num_factors = len(factor_dic)
            pow = {factor: 0 for factor in factor_dic}
            finished = False
            while not finished:
                proper_divisors.append(functools.reduce(lambda x, y: x * y, [factor ** pow[factor] for factor in factor_dic], 1))
                i = 0
                while True:
                    pow[primes[i]] += 1
                    if pow[primes[i]] <= factor_dic[primes[i]]:
                        break
                    pow[primes[i]] = 0
                    i += 1
                    if i >= num_factors:
                        finished = True
                        break
            proper_divisors_dic[path[-1]] = sum(proper_divisors) - path[-1]
            path.append(sum(proper_divisors) - path[-1])
            
        if len(path) >= 3 and path[-1] == path[-3]:
            amicable.add(path[-1])
            amicable.add(path[-2])
ans = sum(amicable)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")