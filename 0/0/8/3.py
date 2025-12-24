import time
from utils.algorithm import dijkstra_grid

N = open("matrix.txt", "r").read()

t0 = time.time()
grid = [[int(i) for i in row.split(",")] for row in N.split("\n")]
max_path = sum(map(sum, grid))
ans = grid[0][0] + dijkstra_grid(grid, lambda p1, p2: grid[p2[1]][p2[0]] if abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) == 1 else max_path)[-1][-1]
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")