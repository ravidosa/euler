import time

N = open("triangle.txt", "r").read()

t0 = time.time()
grid = [[int(i) for i in row.split(" ")] for row in N.split("\n")]

for i in range(len(grid) - 2, -1, -1):
    for j in range(i + 1):
        grid[i][j] += max(grid[i + 1][j], grid[i + 1][j + 1])
ans = grid[0][0]
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")