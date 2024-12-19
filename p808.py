import time, math, itertools
from utils.primes import is_prime

N = 50

t0 = time.time()
reversible_prime_squares = set()
r = 1
while len(reversible_prime_squares) < N:
    for digits in itertools.product(range(4), repeat=r):
        i = int("".join([str(digit) for digit in digits]))
        square = i ** 2
        if str(square) != str(square)[::-1]:
            if is_prime(i):
                if math.sqrt(int(str(square)[::-1])).is_integer():
                    if is_prime(int(math.sqrt(int(str(square)[::-1])))):
                        reversible_prime_squares.add(square)
                        if len(reversible_prime_squares) == N:
                            break
    r += 1
ans = sum(reversible_prime_squares)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")