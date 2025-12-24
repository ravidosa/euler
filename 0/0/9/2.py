import time
from utils.digits import sum_digits

N = 10000000

t0 = time.time()
chain = {1: 1, 89: 89}
ans = 1
for i in range(2, N):
    seq = [i]
    while seq[-1] not in chain:
        seq.append(sum_digits(seq[-1], lambda x: x ** 2))
    for j in range(len(seq) - 1):
        chain[seq[j]] = chain[seq[-1]]
    if chain[seq[-1]] == 89:
        ans += len(seq) - 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")