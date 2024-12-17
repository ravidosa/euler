import time

N = 4503599627370517
M = 1504170715041707

t0 = time.time()
coin = M
mincoin = coin
ans = coin
for i in range(2, N):
    if i % 100000 == 0:
        print(i)
    coin = (coin * M) % N
    if coin < mincoin:
        ans += coin
        mincoin = coin
    if coin == 1:
        break
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")