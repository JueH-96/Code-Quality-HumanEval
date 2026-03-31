def max_fill(grid, capacity):
    import math
    """
    Calculate the minimum number of times buckets need to be lowered to empty all wells.

    Args:
        grid (List[List[int]]): 2-D grid where each row represents a well and each 1 is a unit of water.
        capacity (int): Capacity of each bucket.

    Returns:
        int: Total number of bucket lowerings required.
    """
    total_lowerings = 0
    for row in grid:
        water_units = sum(row)
        # Add the number of full/partial buckets needed for this well.
        total_lowerings += math.ceil(water_units / capacity) if water_units else 0
    return total_lowerings