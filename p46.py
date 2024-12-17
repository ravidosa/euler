import time, math

def is_prime(i):
    if i <= 1:
        return False
    for p in range(2, math.floor(math.sqrt(i)) + 1):
        if i % p == 0:
            return False
    return True

t0 = time.time()
i = 9
while True:
    if i % 2 == 1 and not is_prime(i):
        conjecture = False
        for j in range(math.ceil(math.sqrt(i / 2))):
            if is_prime(i - 2 * j ** 2):
                conjecture = True
                break
        if not conjecture:
            ans = i
            break
    i += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")