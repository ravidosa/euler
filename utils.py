import math

def is_prime(i):
    if i <= 1:
        return False
    for p in range(2, math.floor(math.sqrt(i)) + 1):
        if i % p == 0:
            return False
    return True