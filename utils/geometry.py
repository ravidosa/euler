import math

def herons(a, b, c):
    if a == 0 or b == 0 or c == 0 or a + b <= c or a + c <= b or b + c <= a:
        return 0.0
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))