import time, itertools

N = 5

t0 = time.time()
ans = 0
for comb in itertools.permutations(range(1, N * 2 + 1)):
    lines = [(comb[2 * i], comb[2 * i + 1], comb[(2 * i + 3) % (N * 2)]) for i in range(N)]
    line_sum = list(map(sum, lines))
    if all(map(lambda s: s == line_sum[0], line_sum)):
        lines = lines[lines.index(min(lines)):] + lines[:lines.index(min(lines))]
        concat = "".join(map(lambda l: "".join(map(str, l)), lines))
        if len(concat) == 16:
            ans = max(ans, int(concat))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")