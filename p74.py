import time, math
from utils.digits import sum_digits

N = 1000000

t0 = time.time()
ans = 0
digit_factorial_chain_dic = {}
for i in range(1, N):
    if i not in digit_factorial_chain_dic:
        path = [i]
        while path[-1] not in path[:-1] and path[-1] not in digit_factorial_chain_dic:
            path.append(sum_digits(path[-1], math.factorial))
        if path[-1] in digit_factorial_chain_dic:
            for ind, p in enumerate(path[:-1]):
                digit_factorial_chain_dic[p] = len(path) - ind + digit_factorial_chain_dic[path[-1]] - 1
                if digit_factorial_chain_dic[p] == 60:
                    ans += 1
        else:
            rep = path.index(path[-1])
            for ind, p in enumerate(path[:rep]):
                digit_factorial_chain_dic[p] = len(path) - ind - 1
                if digit_factorial_chain_dic[p] == 60:
                    ans += 1
            for p in path[rep:-1]:
                digit_factorial_chain_dic[p] = len(path) - rep - 1
            if len(path) - rep - 1 == 60:
                ans += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")