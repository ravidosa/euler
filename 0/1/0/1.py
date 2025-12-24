import time, functools

N = 10
u = lambda n: 1 - n + n ** 2 - n ** 3 + n ** 4 - n ** 5 + n ** 6 - n ** 7 + n ** 8 - n ** 9 + n ** 10

def newton(f_i):
    res = f_i[0]
    k = len(f_i)
    for l in range(k - 1, 0, -1):
        for i in range(l):
            f_i[i] = (f_i[i + 1] - f_i[i]) // (k - l)
        res += f_i[0] * functools.reduce(lambda a, b: a * b, map(lambda i: k - i, range(k - l)))
    return res

t0 = time.time()
ans = 0
for i in range(1, N + 1):
    ans += newton([u(j) for j in range(1, i + 1)])
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")