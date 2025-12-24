import time, itertools
from utils.logic import reverse_polish

N = 4

t0 = time.time()
max_consecutive = 0
ans = ""
for digits in itertools.combinations(range(10), N):
    targets = set()
    dig_str = "".join(map(str, digits))
    for operations in itertools.product("/*+-", repeat=N - 1):
        op_str = "".join(operations)
        for expression in itertools.permutations(dig_str + op_str):
            val = reverse_polish(expression)
            if val and val.is_integer() and val > 0:
                targets.add(int(val))
    consecutive = 1
    while consecutive + 1 in targets:
        consecutive += 1
    if consecutive > max_consecutive:
        max_consecutive = consecutive
        ans = dig_str
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")
