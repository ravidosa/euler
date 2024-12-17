import time, math

N = 1000000

def is_prime(i):
    if i <= 1:
        return False
    for p in range(2, math.floor(math.sqrt(i)) + 1):
        if i % p == 0:
            return False
    return True

t0 = time.time()
ans = 0
for i in range(2, N):
    if is_prime(i):
        circular = True
        for j in range(1, len(str(i))):
            circ = int(str(i)[j:] + str(i)[:j])
            if not is_prime(circ):
                circular = False
                break
        if circular:
            ans += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")