def minPath(grid, k):
    from heapq import heappop, heappush
    import sys

    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Priority queue to store the paths based on their lexicographical order of values
    pq = []
    
    # Initialize the priority queue with all possible starting positions
    for i in range(n):
        for j in range(n):
            heappush(pq, ([grid[i][j]], i, j, 1))  # (current path list, x, y, length of path)
    
    # BFS-like approach using a priority queue to always expand the lexicographically smallest path
    while pq:
        path, x, y, length = heappop(pq)
        
        # If the path length equals k, return the path
        if length == k:
            return path
        
        # Explore all possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                # Append the new cell value and continue
                new_path = path + [grid[nx][ny]]
                heappush(pq, (new_path, nx, ny, length + 1))