def minPath(grid, k):
    n = len(grid)
    
    # Find the position of 1 in the grid
    start_row, start_col = 0, 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                start_row, start_col = i, j
                break
    
    # Directions for neighbors (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    path = []
    current_row, current_col = start_row, start_col
    
    for _ in range(k):
        path.append(grid[current_row][current_col])
        
        if len(path) == k:  # We've collected k values
            break
            
        # Find the neighbor with minimum value
        min_val = float('inf')
        next_row, next_col = current_row, current_col
        
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            
            # Check if the new position is within bounds
            if 0 <= new_row < n and 0 <= new_col < n:
                if grid[new_row][new_col] < min_val:
                    min_val = grid[new_row][new_col]
                    next_row, next_col = new_row, new_col
        
        current_row, current_col = next_row, next_col
    
    return path