import time, math

t0 = time.time()
drills = 100
drill_depths = [i + 1 for i in range(drills)]
for _ in range(drills):
    drill_depths[0] = math.log(drill_depths[1])
    for i in range(1, drills - 1):
        drill_depths[i] = drill_depths[i - 1] + math.log(drill_depths[i + 1])
    ans = drill_depths[0] + sum(map(lambda i: drill_depths[i] * math.exp(-drill_depths[i - 1]), range(1, drills)))
ans = round(ans, 9)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")