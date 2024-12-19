import time, itertools

t0 = time.time()
ans = 0
squares = [i ** 2 for i in range(1, 10)]
for pair in itertools.combinations(itertools.combinations(range(10), 6), 2):
    cube1, cube2 = pair
    valid = True
    for square in squares:
        d1, d2 = square // 10, square % 10
        if ((d1 in cube1 or (d1 in [6, 9] and 15 - d1 in cube1)) and (d2 in cube2 or (d2 in [6, 9] and 15 - d2 in cube2))):
            continue
        if ((d1 in cube2 or (d1 in [6, 9] and 15 - d1 in cube2)) and (d2 in cube1 or (d2 in [6, 9] and 15 - d2 in cube1))):
            continue
        else:
            valid = False
            break
    if valid:
        ans += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")