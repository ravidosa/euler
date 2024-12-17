import time

N = 4000000

t0 = time.time()
ans = 2

an_1 = 1
an = 2

while an < N:
    an_1, an = an, an_1 + an
    if an % 2 == 0:
        ans += an
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")