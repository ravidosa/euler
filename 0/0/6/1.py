import time, itertools
from utils.sequences import is_triangular, is_square, is_pentagonal, is_hexagonal, is_heptagonal, is_octogonal

t0 = time.time()
shapes = []
for i in range(1000, 10000):
    if is_triangular(i):
        shapes.append((i, 3))
    if is_square(i):
        shapes.append((i, 4))
    if is_pentagonal(i):
        shapes.append((i, 5))
    if is_hexagonal(i):
        shapes.append((i, 6))
    if is_heptagonal(i):
        shapes.append((i, 7))
    if is_octogonal(i):
        shapes.append((i, 8))
cyclic = {}
for pair in itertools.permutations(shapes, 2):
    if pair[0][0] != pair[1][0] and pair[0][1] != pair[1][1]:
        if pair[0][0] % 100 == pair[1][0] // 100:
            cyclic[pair[0]] = cyclic.get(pair[0], []) + [pair[1]]
for oct in filter(is_octogonal, range(1000, 10000)):
    for sh1 in cyclic.get((oct, 8), []):
        for sh2 in cyclic.get(sh1, []):
            for sh3 in cyclic.get(sh2, []):
                for sh4 in cyclic.get(sh3, []):
                    for sh5 in cyclic.get(sh4, []):
                        if sh5[0] % 100 == oct // 100:
                            if len(set([sh1[1], sh2[1], sh3[1], sh4[1], sh5[1], 8])) == 6:
                                ans = oct + sh1[0] + sh2[0] + sh3[0] + sh4[0] + sh5[0]
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")