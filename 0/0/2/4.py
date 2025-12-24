import time, math

N = 1000000

t0 = time.time()
digits = [i for i in range(10)]
position = N - 1
ans = ""

for i in range(9, -1, -1):
    digit = digits[position // math.factorial(i)]
    ans += str(digit)
    digits.remove(digit)
    position %= math.factorial(i)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")