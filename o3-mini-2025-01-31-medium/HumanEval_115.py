def max_fill(grid, capacity):
    import math
    total_lowers = 0
    for well in grid:
        water_units = sum(well)
        total_lowers += math.ceil(water_units / capacity)
    return total_lowers