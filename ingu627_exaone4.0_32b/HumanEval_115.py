def max_fill(grid, capacity):
    import math
    total_trips = 0
    for well in grid:
        w = sum(well)
        if w == 0:
            trips = 0
        else:
            trips = (w + capacity - 1) // capacity
        total_trips += trips
    return total_trips