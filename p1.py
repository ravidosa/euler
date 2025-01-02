import time, itertools, math

N = 1000
div_by = [3, 5]

t0 = time.time()
ans = 0
for intersection in range(1, len(div_by) + 1):
    for subset in itertools.combinations(div_by, intersection):
        a1 = math.lcm(*subset)
        n = (N - 1) // a1
        ans += (-1) ** (intersection + 1) * ((n + 1) * a1 * n // 2)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")