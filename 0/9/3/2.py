import time

N = 16

t0 = time.time()
ans = 0
for i in range(9, 10 ** (N // 2)):
    sq = i ** 2
    dec = 10 ** (len(str(sq)) // 2)
    if (i * (dec - i)) % (dec - 1) == 0 or (i * (dec * 10 - i)) % (dec * 10 - 1) == 0:
        for j in range(1, len(str(sq))):
            if int(str(sq)[:j]) + int(str(sq)[j:]) == i and str(sq)[j] != "0":
                ans += sq
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")