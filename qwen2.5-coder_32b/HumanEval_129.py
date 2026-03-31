def minPath(grid, k):
    from heapq import heappush, heappop
    
    N = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Priority queue to store paths with their current lexicographical order
    pq = []
    
    # Initialize the priority queue with all starting positions
    for i in range(N):
        for j in range(N):
            heappush(pq, (grid[i][j], [(i, j)]))
    
    # Perform a modified BFS/DFS using the priority queue
    while pq:
        current_value, path = heappop(pq)
        
        if len(path) == k:
            return [grid[x][y] for x, y in path]
        
        last_x, last_y = path[-1]
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = last_x + dx, last_y + dy
            
            if 0 <= nx < N and 0 <= ny < N:
                new_path = path + [(nx, ny)]
                new_value = current_value * (N * N) + grid[nx][ny]
                heappush(pq, (new_value, new_path))