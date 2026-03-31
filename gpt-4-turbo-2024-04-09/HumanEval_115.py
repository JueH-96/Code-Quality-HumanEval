def max_fill(grid, capacity):
    import math
    total_buckets = 0
    for row in grid:
        water_units = sum(row)
        total_buckets += math.ceil(water_units / capacity)
    return total_buckets