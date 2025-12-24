import time, math, itertools

N_A = 100
N_B = 100

t0 = time.time()
ans = len(set([a ** b for a in range(2, N_A + 1) for b in range(2, N_B + 1)]))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")

t0 = time.time()
is_power = []
highest_power = {}
for a in range(2, N_A + 1):
    if a not in is_power:
        highest_power[a] = math.floor(math.log(N_A, a))
        is_power.extend(map(lambda exp: a ** exp, range(2, highest_power[a] + 1)))

ans = sum(map(lambda a: len(set(map(lambda pair: pair[0] * pair[1], itertools.product(range(2, N_B + 1), range(1, highest_power[a] + 1))))), highest_power.keys()))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")