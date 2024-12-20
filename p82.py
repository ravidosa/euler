import time

N = open("matrix.txt", "r").read()

t0 = time.time()
grid = [[int(i) for i in row.split(",")] for row in N.split("\n")]
max_path = sum(map(sum, grid))
grid_ = [[max_path if i != 0 else grid[j][i] for i in range(len(grid[0]))] for j in range(len(grid))]
for i in range(1, len(grid[0])):
    for j in range(len(grid)):
        grid_[j][i] = grid_[j][i - 1]
        up = 0
        for k in range(j - 1, -1, -1):
            grid_[j][i] = min(grid_[j][i], up + grid[k][i] + grid_[k][i - 1])
            up += grid[k][i]
        down = 0
        for k in range(j + 1, len(grid)):
            grid_[j][i] = min(grid_[j][i], down + grid[k][i] + grid_[k][i - 1])
            down += grid[k][i]
        grid_[j][i] += grid[j][i]
ans = min(map(lambda row: row[-1], grid_))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")