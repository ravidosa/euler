import time, itertools
from utils.sets import powerset

sets = open("sets.txt", "r").read()
N = len(sets)

t0 = time.time()
ans = 0
sets = sets.split("\n")
for s in sets:
    s = set(map(int, s.split(",")))
    special = True
    for sb, sc in itertools.combinations(map(set, powerset(s)), 2):
        if len(sb.intersection(sc)) == 0:
            if (sum(sb) == sum(sc)) or (len(sb) > len(sc) and sum(sb) <= sum(sc)) or (len(sc) > len(sb) and sum(sc) <= sum(sb)):
                special = False
                break
    if special:
        ans += sum(s)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")