import time, math

N = 4

t0 = time.time()
N_distinct = [False] * N
i = 2
while True:
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
    N_distinct[0:N - 1] = N_distinct[1:N]
    N_distinct[-1] = (len(factor_dic) == N)
    if all(N_distinct):
        ans = i - N + 1
        break
    i += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")