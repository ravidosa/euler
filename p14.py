import time

N = 1000000

t0 = time.time()
chain = {1: 1}
for i in range(2, N):
    seq = [i]
    while seq[-1] not in chain:
        if seq[-1] % 2 == 0:
            seq.append(seq[-1] // 2)
        else:
            seq.append(3 * seq[-1] + 1)
    for j in range(len(seq)):
        chain[seq[j]] = len(seq) - 1 - j + chain[seq[-1]]
ans = max(chain, key=chain.get)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")