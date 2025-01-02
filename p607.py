import time, math

N = [10, 9, 8, 7, 6, 5]
D = 100
W = 50

t0 = time.time()
path = (D / math.sqrt(2) - W) / 2
marsh = W / (len(N) - 1)
low = 0
high = math.pi / 2
horiz = 0
while abs(horiz - D / math.sqrt(2)) >= 10 ** -10:
    mid = (low + high) / 2
    horiz = 2 * path * math.tan(mid)
    for i in range(1, len(N)):
        horiz += marsh * math.tan(math.asin(math.sin(mid) * N[i] / N[0]))
    if horiz < D / math.sqrt(2):
        low = mid
    else:
        high = mid
ans = 2 * path / math.cos(mid) / N[0]
for i in range(1, len(N)):
    ans += marsh / math.cos(math.asin(math.sin(mid) * N[i] / N[0])) / N[i]
ans = round(ans, 10)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")