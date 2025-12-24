import time, math, itertools

N = 1000000

t0 = time.time()
ans = 0
solutions = 0
while solutions < N:
    ans += 1
    for sides in itertools.combinations_with_replacement(range(1, ans + 1), 2):
        a, b = sides
        if min(math.sqrt(a ** 2 + (b + ans) ** 2), math.sqrt(b ** 2 + (a + ans) ** 2), math.sqrt(ans ** 2 + (a + b) ** 2)).is_integer():
            solutions += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")