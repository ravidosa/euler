import time, math

N = 100

t0 = time.time()
fac = math.factorial(N)
for i in range(int(math.log(N, 5))):
    fac //= (10 ** (N // (5 ** (i + 1))))
ans = 0
while fac > 0:
    ans += (fac % 10)
    fac //= 10
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")