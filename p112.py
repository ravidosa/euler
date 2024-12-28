import time
from utils.digits import increasing, decreasing

N = 0.99

t0 = time.time()
bouncy = 0
ans = 99
while bouncy / ans != N:
    ans += 1
    if not increasing(ans) and not decreasing(ans):
        bouncy += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")