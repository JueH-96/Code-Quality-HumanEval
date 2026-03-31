def minPath(grid, k):
    """
    Returns the lexicographically minimum path of length k on the grid.
    """
    n = len(grid)
    # Locate the cell with the minimum value in the entire grid
    min_val = grid[0][0]
    start_r = start_c = 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] < min_val:
                min_val = grid[r][c]
                start_r, start_c = r, c

    path = [min_val]
    r, c = start_r, start_c
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for _ in range(k - 1):
        best_val = None
        best_pos = None
        # Choose the neighbor with the smallest value
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                val = grid[nr][nc]
                if best_val is None or val < best_val:
                    best_val = val
                    best_pos = (nr, nc)
        path.append(best_val)
        r, c = best_pos

    return path