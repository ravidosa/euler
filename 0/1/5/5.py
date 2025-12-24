import time, math, itertools, functools

N = 18

t0 = time.time()
config = [set()]
config[0].add((1,1))
for i in range(1, N):
    config.append(set())
    for j in range(i // 2 + 1):
        for ca, cb in itertools.product(config[j], config[i - j - 1]):
            n, d = ca[0] * cb[1] + ca[1] * cb[0], ca[1] * cb[1]
            gcd = math.gcd(n, d)
            config[i].add((n // gcd, d // gcd))
            n, d = ca[0] * cb[0], ca[0] * cb[1] + ca[1] * cb[0]
            gcd = math.gcd(n, d)
            config[i].add((n // gcd, d // gcd))
ans = len(functools.reduce(lambda a, b: a.union(b), config))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")