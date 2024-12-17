import time, math, itertools

t0 = time.time()
ans = 2
for n in [7, 4]:
    for permutation in itertools.permutations([str(i) for i in range(1, n + 1)]):
        pandigital = int("".join(permutation))
        curr = pandigital
        p = 2
        while p <= math.sqrt(curr):
            if curr % p == 0:
                curr //= p
            else:
                p += 1
        if curr == pandigital:
            ans = max(ans, pandigital)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")