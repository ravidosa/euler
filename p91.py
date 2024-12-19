import time, itertools

N_1, N_2 = 0, 50

t0 = time.time()
ans = 0
for p1, p2 in itertools.combinations(itertools.product(range(N_1, N_2 + 1), repeat=2), 2):
    if p1 == (0, 0) or p2 == (0, 0):
        continue
    s1 = p2
    s2 = p1
    s3 = (p1[0] - p2[0], p1[1] - p2[1])

    if s1[0] * s2[0] + s1[1] * s2[1] == 0 or s1[0] * s3[0] + s1[1] * s3[1] == 0 or s2[0] * s3[0] + s2[1] * s3[1] == 0:
        ans += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")