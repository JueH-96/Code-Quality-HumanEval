def max_fill(grid, capacity):
    num_buckets = 0
    for row in grid:
        num_wells = sum(row)
        if num_wells > 0:
            num_buckets += math.ceil(num_wells/capacity)
    return num_buckets