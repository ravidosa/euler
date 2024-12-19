import time
from utils.primes import is_prime

N = 5

t0 = time.time()
ans = None
primes_check = [[3], [], []]
pairs = {}
cliques = {}
p = 5
bound = 10000
while not ans or p < bound:
    clique_candidates = set()
    for prime in primes_check[0] + primes_check[p % 3]:
        if is_prime(int(str(p) + str(prime))) and is_prime(int(str(prime) + str(p))):
            pairs[p] = pairs.get(p, set()).union(set([prime]))
            for prev in clique_candidates:
                if prev in pairs.get(prime, set()):
                    cliques[p] = cliques.get(p, []) + [set([prev, prime, p])]
                    if N == 3:
                        ans = min(ans, prev + prime + p) if ans else prev + prime + p
            clique_candidates.add(prime)
    if len(clique_candidates) >= N - 1 and (not ans or p + sum(sorted(clique_candidates)[:N - 1]) < ans) :
        for candidate in clique_candidates:
            for clique in cliques.get(candidate, []):
                if clique.issubset(clique_candidates):
                    cliques[p].append(clique.union({p}))
                    if len(clique) == N - 1:
                        ans = min(ans, sum(clique) + p) if ans else sum(clique) + p
    primes_check[p % 3].append(p)
    p += 1
    while not is_prime(p):
        p += 1
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")