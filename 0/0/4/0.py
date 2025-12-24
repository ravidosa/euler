import time, math

digit_index = [1, 10, 100, 1000, 10000, 100000, 1000000]

t0 = time.time()
ans = 1
for index in digit_index:
    i = 1
    while sum(map(lambda j: 9 * 10 ** (j - 1) * j, range(1, i + 1))) < index:
        i += 1
    nindex = index - sum(map(lambda j: 9 * 10 ** (j - 1) * j, range(1, i)))
    ans *= int(str(math.ceil(nindex / i) + (0 if i == 1 else int("9" * (i - 1))))[(nindex - 1) % i])
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")