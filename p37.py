import time, math

def is_prime(i):
    if i <= 1:
        return False
    for p in range(2, math.floor(math.sqrt(i)) + 1):
        if i % p == 0:
            return False
    return True

t0 = time.time()
truncatable = []
i = 11
while len(truncatable) < 11:
    if [int(digit) % 2 == 1 for digit in str(i)]:
        if is_prime(i):
            if all([is_prime(int(str(i)[j:])) for j in range(1, len(str(i)))]) and all([is_prime(int(str(i)[:j])) for j in range(1, len(str(i)))]):
                truncatable.append(i)
    i += 1
ans = sum(truncatable)
print(truncatable)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")