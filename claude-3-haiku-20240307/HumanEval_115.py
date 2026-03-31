def max_fill(grid, capacity):
    total_water = sum(sum(row) for row in grid)
    if total_water <= capacity:
        return total_water
    
    rows, cols = len(grid), len(grid[0])
    total_fills = 0
    
    for col in range(cols):
        water_in_col = sum(row[col] for row in grid)
        total_fills += math.ceil(water_in_col / capacity)
    
    return total_fills