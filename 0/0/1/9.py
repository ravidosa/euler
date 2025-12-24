import time

N1 = 1901
N2 = 2000

t0 = time.time()
ans = 0
day = 2
for year in range(N1, N2 + 1):
    s = 0
    for month in range(12):
        if day == 0:
            ans += 1
            s += 1
        day += (30 if month in [3, 5, 8, 10] else 31 if month != 1 else 28 + (1 if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0) else 0))
        day %= 7
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")