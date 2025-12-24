import time, itertools

N = 7
K = 1
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:N]

t0 = time.time()
maximix = []
for arr in itertools.permutations(alph):
    arr_ = "".join(arr)
    rot = 0
    for a in alph:
        if arr_.index(a) != alph.index(a):
            if arr_.index(a) != N - 1:
                arr_ = arr_[:arr_.index(a)] + arr_[arr_.index(a):][::-1]
                rot += 1
            arr_ = arr_[:alph.index(a)] + arr_[alph.index(a):][::-1]
            rot += 1
    if rot == 2 * (N - 1) - 1:
        maximix.append("".join(arr))
ans = sorted(maximix)[K - 1]
print(sorted(maximix))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")