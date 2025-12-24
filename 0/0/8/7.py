import time, math
from utils.primes import generate_primes_up_to

N = 50000000

t0 = time.time()
nums = set()
primes = generate_primes_up_to(math.floor(math.sqrt(N)))
for square in map(lambda i: i ** 2, primes):
    for cube in map(lambda i: i ** 3, primes):
        if square + cube > N:
            break
        for quart in map(lambda i: i ** 4, primes):
            if square + cube + quart > N:
                break
            if square + cube + quart < N:
                nums.add(square + cube + quart)
ans = len(nums)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")