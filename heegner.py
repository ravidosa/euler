import time, mpmath

N = 1000

t0 = time.time()
minerr = 1
ans = 0
mpmath.mp.prec = 175
for i in range(-N, N + 1):
    if i < 0 or not float(mpmath.mp.sqrt(i)).is_integer():
        value = mpmath.mp.cos(mpmath.mp.pi * mpmath.mp.sqrt(i)).real
        err = min(value % 1, 1 - (value % 1))
        if err < minerr:
            minerr = err
            ans = i
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")