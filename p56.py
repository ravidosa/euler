import time

N_A = 100
N_B = 100

t0 = time.time()
ans = max([sum([int(digit) for digit in str(a ** b)]) for a in range(2, N_A) for b in range(2, N_B)])
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")