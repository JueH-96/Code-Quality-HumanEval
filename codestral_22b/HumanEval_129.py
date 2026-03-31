def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k,
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    Finds the minimum path of length k in the grid using DFS.
    """

    # Directions for moving from current cell (up, down, left, right)
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    n = len(grid)

    def dfs(i, j, k, path):
        # If path length is k, return the path
        if k == 0:
            return path

        min_path = None
        # Explore all possible directions
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            # Check if new position is valid
            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > path[-1]:
                path.append(grid[ni][nj])
                candidate = dfs(ni, nj, k - 1, path)
                # Update minimum path if current path is smaller
                if min_path is None or (candidate is not None and candidate < min_path):
                    min_path = candidate
                path.pop()
        return min_path

    min_path = None
    # Start DFS from each cell
    for i in range(n):
        for j in range(n):
            path = [grid[i][j]]
            candidate = dfs(i, j, k - 1, path)
            if min_path is None or (candidate is not None and candidate < min_path):
                min_path = candidate
    return min_path