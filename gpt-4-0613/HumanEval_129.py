def minPath(grid, k):
    import heapq
    N = len(grid)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    heap = [(grid[i][j], i, j, [grid[i][j]]) for i in range(N) for j in range(N)]
    heapq.heapify(heap)
    while heap:
        val, x, y, path = heapq.heappop(heap)
        if len(path) == k:
            return path
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                visited.add((nx, ny))
                heapq.heappush(heap, (grid[nx][ny], nx, ny, path + [grid[nx][ny]]))