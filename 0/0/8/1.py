import time

N = open("matrix.txt", "r").read()

t0 = time.time()
grid = [[int(i) for i in row.split(",")] for row in N.split("\n")]
max_path = sum(map(sum, grid))
grid_ = [[max_path for _ in range(len(grid[0]))] for __ in range(len(grid))]
grid_[0][0] = grid[0][0]

for i in range(0, len(grid) + len(grid[0]) - 1):
    for j in range(max(0, i + 1 - len(grid)), min(i + 1, len(grid[0]))):
        if 0 <= j < len(grid) and 0 <= i - j < len(grid[0]):
            x, y = i - j, j
            if x < len(grid[0]) - 1:
                grid_[y][x + 1] = min(grid_[y][x + 1], grid_[y][x] + grid[y][x + 1])
            if y < len(grid) - 1:
                grid_[y + 1][x] = min(grid_[y + 1][x], grid_[y][x] + grid[y + 1][x])
ans = grid_[-1][-1]
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")