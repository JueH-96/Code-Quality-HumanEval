import heapq

def minPath(grid, k):
    n = len(grid)
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Priority queue elements are tuples: (current_path, x, y)
    # The priority is the current_path itself, which is a list. Since tuples are compared lexicographically,
    # we can push the path as a tuple into the heap.
    heap = []
    
    # Initialize the heap with all possible starting cells
    for i in range(n):
        for j in range(n):
            heapq.heappush(heap, ( (grid[i][j],), i, j ) )
    
    while heap:
        current_path, x, y = heapq.heappop(heap)
        if len(current_path) == k:
            return list(current_path)
        # Explore all four neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                new_path = current_path + (grid[nx][ny],)
                heapq.heappush(heap, (new_path, nx, ny))