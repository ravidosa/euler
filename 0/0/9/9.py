import time, math

powers = open("base_exp.txt", "r").read()
N = len(powers)

t0 = time.time()
ans = 0
max_log = 0
powers = map(lambda exp: (int(exp.split(",")[0]), int(exp.split(",")[1])), powers.split("\n"))
for ind, power in enumerate(powers):
    base, exp = power
    if exp * math.log(base) > max_log:
        max_log = exp * math.log(base)
        ans = ind + 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")