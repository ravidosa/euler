import time, math

N = 1000

t0 = time.time()

an_1 = 0
an = 1
ans = 1

while math.log10(an) + 1 < N:
    an_1, an = an, an_1 + an
    ans += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")

t0 = time.time()
phi = (1 + math.sqrt(5)) / 2
ans = math.ceil((N - 1 + math.log10(5) / 2) / math.log10(phi))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")