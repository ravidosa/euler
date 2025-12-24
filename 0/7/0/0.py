import time

N = 4503599627370517
M = 1504170715041707

t0 = time.time()
thresh = 10 ** 8
mincoin = N
ans = 0
M_inv = pow(M, -1, N)
ind = 0
while True:
    ind += 1
    coin = (M * ind) % N
    if coin < mincoin:
        ans += coin
        mincoin = coin
    if mincoin <= thresh:
        break
coin = 1
maxindex = N
while coin != mincoin:
    i = (M_inv * coin) % N
    if i < maxindex:
        maxindex = i
        ans += coin
    coin += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")