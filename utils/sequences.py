import math

def triangular(n):
    return n * (n + 1) // 2

def is_triangular(n):
    return ((-1 + math.sqrt(1 + 8 * n)) / 2).is_integer()

def triangular_under(n):
    return triangular(triangular_under_index(n))

def triangular_under_index(n):
    return math.floor((-1 + math.sqrt(1 + 8 * n)) / 2)

def square(n):
    return n ** 2

def is_square(n):
    return (math.sqrt(n)).is_integer()

def square_under(n):
    return square(square_under_index(n))

def square_under_index(n):
    return math.floor(math.sqrt(n))

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

def heptagonal(n):
    return n * (5 * n - 3) // 2

def is_heptagonal(n):
    return ((3 + math.sqrt(9 + 40 * n)) / 10).is_integer()

def heptagonal_under(n):
    return heptagonal(heptagonal_under_index(n))

def heptagonal_under_index(n):
    return math.floor((3 + math.sqrt(9 + 40 * n)) / 10)

def octogonal(n):
    return n * (3 * n - 2)

def is_octogonal(n):
    return ((2 + math.sqrt(4 + 12 * n)) / 6).is_integer()

def octogonal_under(n):
    return octogonal(octogonal_under_index(n))

def octogonal_under_index(n):
    return math.floor((2 + math.sqrt(4 + 12 * n)) / 6)