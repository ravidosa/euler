import time

queries = open("keylog.txt", "r").read()
N = len(queries)
M = queries.index("\n")

t0 = time.time()
queries = queries.split("\n")
order = {}
for query in queries:
    order[query[0]] = order.get(query[0], set([])).union(set([query[1], query[2]]))
    order[query[1]] = order.get(query[1], set([])).union(set([query[2]]))
ans = "".join(key for key in sorted(order.keys(), key=lambda k: len(order[k]), reverse=True))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")