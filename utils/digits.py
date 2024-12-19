import math, itertools

def is_permutations(terms):
    if len(terms) <= 1:
        return True
    return all(map(lambda pair: "".join(sorted(str(pair[0]))) == "".join(sorted(str(pair[1]))), itertools.combinations(terms, 2)))

def sum_digits(n, func=lambda x: x):
    return sum(map(lambda x: func(int(x)), str(n)))

def odd_digits(n):
    return all([int(digit) % 2 == 1 for digit in str(n)])

def even_digits(n):
    return all([int(digit) % 2 == 0 for digit in str(n)])

def is_pandigital(a, b, n):
    digits = "0123456789"
    return "".join(sorted(str(n))) == digits[a:b + 1]

def generate_pandigital(a, b):
    return map(lambda perm: int("".join(perm)), itertools.permutations([str(i) for i in range(a, b + 1)]))

def square_root_digits(n, precision):
    dig_before = str(float(n)).index(".")
    dig_after = len(str(float(n))) - dig_before - 1
    pairs = [math.floor(n // 100 ** i) % 100 for i in range(dig_before // 2, -1, -1)] + [math.floor(n * 100 ** i) % 100 for i in range(1, dig_after // 2 + 1)] 
    pairs += [0] * (max(0, (precision - dig_after // 2)) + (1 if pairs[0] == 1 else 0))
    p = 0
    dig = []
    rem = 0
    for pair in pairs:
        c = rem * 100 + pair
        x = 9
        while x * (20 * p + x) > c:
            x -= 1
        y = x * (20 * p + x)
        p = p * 10 + x
        rem = c - y
        dig.append(x)
    return dig