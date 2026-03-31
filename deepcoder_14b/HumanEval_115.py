def max_fill(grid, capacity):
    total = 0
    for row in grid:
        units = sum(row)
        if units == 0:
            continue
        ops = (units + capacity - 1) // capacity
        total += ops
    return total