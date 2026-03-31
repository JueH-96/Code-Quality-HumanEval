def max_fill(grid, capacity):
    import math
    total_lowerings = 0
    for well in grid:
        water_units = sum(well)
        total_lowerings += math.ceil(water_units / capacity)
    return total_lowerings