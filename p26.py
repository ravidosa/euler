import time, math

N = 1000

t0 = time.time()
max_period = 0
ans = 2

for d in range(2, N):
    curr = d
    p = 2
    while p <= math.sqrt(curr):
        if curr % p == 0:
            curr //= p
        else:
            p += 1
    if curr == d and d not in [2, 5]:
        m = math.ceil(math.sqrt(d))
        exp_table = {(10 ** i) % d: i for i in range(1, m + 1)}
        a_m_inv = pow(10, -m, d)
        gamma = 1
        for i in range(m + 1):
            if gamma in exp_table:
                if (i * m + exp_table[gamma]) > max_period:
                    max_period = (i * m + exp_table[gamma])
                    ans = d
                break
            else:
                gamma = (gamma * a_m_inv) % d
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")