def minPath(grid, k):
    from heapq import heappop, heappush

    N = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def neighbors(x, y):
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                yield nx, ny

    min_heap = []
    for i in range(N):
        for j in range(N):
            heappush(min_heap, (grid[i][j], i, j, [grid[i][j]]))

    while min_heap:
        value, x, y, path = heappop(min_heap)
        if len(path) == k:
            return path
        for nx, ny in neighbors(x, y):
            new_path = path + [grid[nx][ny]]
            heappush(min_heap, (grid[nx][ny], nx, ny, new_path))

    return []