import time, math

B = 2
L = 123
N = 678910

t0 = time.time()
ans = -1
count = 0
while count < N:
    ans += 1
    digits = math.floor(10 ** (ans * math.log10(2) - math.floor(ans * math.log10(2)) + math.floor(math.log10(L))))
    if digits == L:
        count += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")