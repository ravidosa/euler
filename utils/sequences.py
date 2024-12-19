import math

def triangular(n):
    return n * (n + 1) // 2

def is_triangular(n):
    return ((-1 + math.sqrt(1 + 8 * n)) / 2).is_integer()

def pentagonal(n):
    return n * (3 * n - 1) // 2

def is_pentagonal(n):
    return ((1 + math.sqrt(1 + 24 * n)) / 6).is_integer()

def hexagonal(n):
    return n * (2 * n - 1)

def is_hexagonal(n):
    return ((1 + math.sqrt(1 + 8 * n)) / 4).is_integer()