def minPath(grid, k):
    N = len(grid)
    from functools import lru_cache

    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    @lru_cache(maxsize=None)
    def dfs(i, j, l):
        # l is the number of cells to cover starting from (i,j)
        if l == 1:
            return (grid[i][j],)
        
        best = None
        # Try all valid neighbors
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                nxt = dfs(ni, nj, l - 1)
                if nxt is not None:
                    candidate = (grid[i][j],) + nxt
                    if best is None or candidate < best:
                        best = candidate
        return best

    best_global = None
    for i in range(N):
        for j in range(N):
            candidate = dfs(i, j, k)
            if candidate is not None:
                if best_global is None or candidate < best_global:
                    best_global = candidate
    return list(best_global)