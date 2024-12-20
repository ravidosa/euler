import math

def triangular(n):
    return n * (n + 1) // 2

def is_triangular(n):
    return ((-1 + math.sqrt(1 + 8 * n)) / 2).is_integer()

def triangular_under(n):
    return triangular(triangular_under_index(n))

def triangular_under_index(n):
    return math.floor((-1 + math.sqrt(1 + 8 * n)) / 2)

def pentagonal(n):
    return n * (3 * n - 1) // 2

def is_pentagonal(n):
    return ((1 + math.sqrt(1 + 24 * n)) / 6).is_integer()

def pentagonal_under(n):
    return pentagonal(pentagonal_under_index(n))

def pentagonal_under_index(n):
    return math.floor((1 + math.sqrt(1 + 24 * n)) / 6)

def hexagonal(n):
    return n * (2 * n - 1)

def is_hexagonal(n):
    return ((1 + math.sqrt(1 + 8 * n)) / 4).is_integer()

def hexagonal_under(n):
    return hexagonal(hexagonal_under_index(n))

def hexagonal_under_index(n):
    return math.floor((1 + math.sqrt(1 + 8 * n)) / 4)