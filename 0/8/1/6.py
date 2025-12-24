import time, math, itertools

N = 2000000
s_0 = 290797
mod = 50515093

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def min_dist(points):
    if len(points) <= 3:
        return min(map(lambda pair: dist(pair[0], pair[1]), itertools.combinations(points, 2)))
    else:
        points.sort(key=lambda p: p[0])
        L = points[:len(points) // 2]
        R = points[len(points) // 2:]
        delta = min(min_dist(L), min_dist(R))
        B_L = [p for p in L if dist(points[len(points) // 2], p) <= delta]
        B_R = [p for p in R if dist(points[len(points) // 2], p) <= delta]
        R.sort(key=lambda p: p[1])
        return min(delta, min(map(lambda pair: dist(pair[0], pair[1]), itertools.product(B_L, B_R)), default=delta))

t0 = time.time()
s_2n = s_0
s_2n_1 = pow(s_2n, 2, mod)
points = [(s_2n, s_2n_1)]
for _ in range(1, N):
    s_2n = pow(s_2n_1, 2, mod)
    s_2n_1 = pow(s_2n, 2, mod)
    points.append((s_2n, s_2n_1))
ans = min_dist(points)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")