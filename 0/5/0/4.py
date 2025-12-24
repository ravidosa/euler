import time, math, itertools

M = 100

t0 = time.time()
ans = 0
for vertices in itertools.product(range(1, M + 1), repeat=4):
    a, b, c, d = vertices
    area = (a * b + b * c + c * d + d * a) / 2
    boundary = math.gcd(a, b) + math.gcd(b, c) + math.gcd(c, d) + math.gcd(d, a)
    interior_lattice = area + 1 - boundary / 2
    if math.sqrt(interior_lattice).is_integer():
        ans += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")