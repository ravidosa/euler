import time

N = open("matrix.txt", "r").read()

t0 = time.time()
grid = [[int(i) for i in row.split(",")] for row in N.split("\n")]

for i in range(1, len(grid) + len(grid[0]) - 1):
    for j in range(max(0, i + 1 - len(grid)), min(i + 1, len(grid[0]))):
        if j == 0 or i - j == len(grid[0]) - 1:
            grid[j][i - j] += grid[j][i - j - 1]
        elif i - j == 0 or j == len(grid) - 1:
            grid[j][i - j] += grid[j - 1][i - j]
        else:
            grid[j][i - j] += min(grid[j - 1][i - j], grid[j][i - j - 1])
ans = grid[-1][-1]
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")