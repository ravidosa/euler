import time, itertools, math

N = 1000
div_by = [3, 5]

# naive implementation with list comprehension
t0 = time.time()
ans = sum(map(lambda i : i if any(map(lambda factor: i % factor == 0, div_by)) else 0, range(1, N)))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")

# using inclusion-exclusion principle, least common multiple, and sum of arithmetic sequence
t0 = time.time()
ans = 0
for intersection in range(1, len(div_by) + 1):
    for subset in itertools.combinations(div_by, intersection):
        a1 = math.lcm(*subset)
        n = (N - 1) // a1
        ans += (-1) ** (intersection + 1) * ((n + 1) * a1 * n // 2)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")