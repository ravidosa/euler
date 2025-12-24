import time, math

N = 10 ** 12

t0 = time.time()
ans = sum(map(lambda i: 2 ** i, range(math.floor(math.log(N, 2)) + 1))) - 5 * sum(map(lambda i: 2 ** i, range(math.floor(math.log(N / 3, 2)) + 1)))
steps = "{0:b}".format(N)
aa = lambda n: n if n <= 2 else 2 * aa(n // 2) if n % 2 == 0 else aa((n - 1) // 2) - 3 * aa((n + 1) // 2)
for i in range(1, len(steps) - 1):
    if steps[i] != steps[i + 1]:
        ans += aa(int(steps[:i] + "01" + "0" * (len(steps) - i - 2), 2))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")