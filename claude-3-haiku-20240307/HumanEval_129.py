def minPath(grid, k):
    n = len(grid)
    visited = set()
    queue = [(i, j, [grid[i][j]]) for i in range(n) for j in range(n)]
    min_path = None

    while queue:
        i, j, path = queue.pop(0)
        if len(path) == k:
            if min_path is None or path < min_path:
                min_path = path
        else:
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    queue.append((ni, nj, path + [grid[ni][nj]]))

    return min_path