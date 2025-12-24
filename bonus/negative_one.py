import time, itertools, math

div_by = [3, 5]

t0 = time.time()
ans = 0
for intersection in range(1, len(div_by) + 1):
    for subset in itertools.combinations(div_by, intersection):
        factor = math.lcm(*subset)
        ans += (-1) ** (intersection + 1) * factor
ans = str(ans // math.gcd(12, ans)) + "/" + str(12 // math.gcd(12, ans))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")