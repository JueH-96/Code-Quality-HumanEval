def max_fill(grid, capacity):
    import math
    total = 0
    for row in grid:
        count = sum(row)
        if count == 0:
            continue
        total += (count + capacity - 1) // capacity
    return total