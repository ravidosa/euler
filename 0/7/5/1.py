import time, mpmath

N = 24

t0 = time.time()
mpmath.mp.prec = 100
theta = "2."
for j in range(1, N + 1):
    for i in range(10):
        ans = (str(theta) + str(i))
        b = [mpmath.mpmathify(ans)]
        for _ in range(j):
            b.append(mpmath.mp.floor(b[-1]) * (b[-1] - mpmath.mp.floor(b[-1]) + 1))
        tau = "2." + "".join([str(int(mpmath.mp.floor(b[i]))) for i in range(1, len(b))])[:j]
        if ans == tau:
            theta += str(i)
            break
print(ans, tau)