import time
from utils.primes import proper_divisors

N = 1000000

t0 = time.time()
max_len = 0
proper_divisors_dic = {1: 0}
for i in range(2, N + 1):
    if i not in proper_divisors_dic:
        path = [i]
        while path[-1] not in proper_divisors_dic and 1 < path[-1] <= N:
            proper_divisors_dic[path[-1]] = sum(proper_divisors(path[-1]))
            path.append(proper_divisors_dic[path[-1]])
            
        if len(path) >= 3 and path[-1] in path[:-1]:
            chain = path[path.index(path[-1]):-1]
            if len(chain) > max_len:
                max_len = len(chain)
                ans = min(chain)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")