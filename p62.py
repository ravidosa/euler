import time
from utils.digits import fingerprint

N = 5

t0 = time.time()
i = 0
fingerprints = {}
while True:
    i += 1
    fp = fingerprint(i ** 3)
    fingerprints[fp] = fingerprints.get(fp, []) + [i ** 3]
    if len(fingerprints[fp]) == N:
        break
ans = min(fingerprints[fp])
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")