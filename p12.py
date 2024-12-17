import time, math, functools

N = 500

t0 = time.time()
factor_dic = {}
divisors = 0

i = (N + 1) // math.sqrt(2)
while divisors < N:
    ans = int((i * (i + 1)) // 2)
    curr = ans
    factor_dic = {}
    p = 2
    while p <= math.sqrt(curr):
        if curr % p == 0:
            curr //= p
            factor_dic[p] = factor_dic.get(p, 0) + 1
        else:
            p += 1
    factor_dic[curr] = factor_dic.get(curr, 0) + 1
    divisors = functools.reduce(lambda x, y: x * (factor_dic[y] + 1), factor_dic, 1)
    i += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")