import time, math, itertools

t0 = time.time()
ans = 0
primes = [2, 3, 5, 7, 11, 13, 17]
for permutation in itertools.permutations([str(i) for i in range(10)]):
    pandigital = "".join(permutation)
    if all([int(pandigital[i + 1:i + 4]) % primes[i] == 0 for i in range(7)]):
        ans += int(pandigital)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")