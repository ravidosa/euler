import time

N = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

t0 = time.time()
coint_count = len(coins)
combos = [0] * (N + 1)
combos[0] = 1
for i in range(coint_count):
    for j in range(coins[i], N + 1):
        combos[j] += combos[j - coins[i]]
ans = combos[N]
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")