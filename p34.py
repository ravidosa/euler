import time, math, scipy

t0 = time.time()
n = math.floor(-(scipy.special.lambertw(-math.log(10) / (10 * math.factorial(9)), -1).real) / math.log(10))
ans = 0
for i in range(3, 10 ** n):
    if i == sum([math.factorial(int(digit)) for digit in str(i)]):
        ans += i
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")