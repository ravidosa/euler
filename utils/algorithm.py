import itertools

def dijkstra_grid(grid, weight, dirs=[(1, 0), (0, 1), (-1, 0), (0, -1)], start=(0, 0), INFINITY=10 ** 10):
    r, c = len(grid), len(grid[0])
    dist = [[INFINITY for _ in range(c)] for __ in range(r)]
    dist[start[1]][start[0]] = 0
    processed = [[False for _ in range(c)] for __ in range(r)]

    for _ in range(r * c):
        check = min(itertools.product(range(c), range(r)), key=lambda p: dist[p[1]][p[0]] if not processed[p[1]][p[0]] else INFINITY)
        processed[check[1]][check[0]] = True
        for d in dirs:
            p = (check[0] + d[0], check[1] + d[1])
            if 0 <= p[0] < c and 0 <= p[1] < r and not processed[p[1]][p[0]]:
                dist[p[1]][p[0]] = min(dist[p[1]][p[0]], dist[check[1]][check[0]] + weight(check, p))
    return dist