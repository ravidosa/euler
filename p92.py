import time

N = 10000000

t0 = time.time()
chain = {1: 1, 89: 89}
for i in range(2, N):
    seq = [i]
    while seq[-1] not in chain:
        seq.append(sum([int(digit) ** 2 for digit in str(seq[-1])]))
    for j in range(len(seq)):
        chain[seq[j]] = chain[seq[-1]]
ans = sum(endpoint == 89 for endpoint in chain.values())
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")