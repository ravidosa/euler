import time

t0 = time.time()
ans = 0
for i in range(10 ** 5):
    concatenation = str(i)
    j = 2
    while len(concatenation) < 9:
        concatenation += str(i * j)
        j += 1
    if "".join(sorted(concatenation)) == "123456789":
            ans = max(ans, int(concatenation))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")