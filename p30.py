import time, math, scipy

N = 5

t0 = time.time()
n = math.floor(-(scipy.special.lambertw(-9 ** (-N) * math.log(10) / 10, -1).real) / math.log(10))
ans = 0
for i in range(2, 10 ** n):
    if i == sum([int(digit) ** N for digit in str(i)]):
        ans += i
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")