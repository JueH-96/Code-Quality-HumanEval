def find_min_path(grid, k):
    if not grid or len(grid) == 0:
        return []
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Find the starting position with the minimum value
    min_val = float('inf')
    start_i, start_j = 0, 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] < min_val:
                min_val = grid[i][j]
                start_i, start_j = i, j
    
    path = [min_val]
    
    current_i, current_j = start_i, start_j
    directions = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]  # up, down, left, right
    
    for _ in range(k - 1):
        min_neighbor_val = float('inf')
        selected_i, selected_j = current_i, current_j
        
        for d in directions:
            ni = current_i + d[0]
            nj = current_j + d[1]
            
            if 0 <= ni < rows and 0 <= nj < cols:
                val = grid[ni][nj]
                if val < min_neighbor_val:
                    min_neighbor_val = val
                    selected_i, selected_j = ni, nj
        
        if min_neighbor_val == float('inf'):
            # No valid moves; break the loop as we cannot proceed further
            break
        else:
            path.append(min_neighbor_val)
            current_i, current_j = selected_i, selected_j
    
    return path

# Example usage:
grid = [
    [5, 4],
    [2, 3]
]

k = 3
print(find_min_path(grid, k))  # Output: [2, 3, 2]