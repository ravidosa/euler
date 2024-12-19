import itertools

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