import time

N = 7

t0 = time.time()
ans = 10 ** (2 * (N - 1)) + 1
for x in range(10 ** N // 11 * 11, 10 ** (N - 1) // 11 * 11, -11):
    for y in range(10 ** N - 1, ans // x, -1):
        prod = x * y
        if str(prod) == str(prod)[::-1]:
            ans = max(ans, prod)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")