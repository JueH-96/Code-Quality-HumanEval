def max_fill(grid, capacity):
    import math
    
    # Calculate total water in all wells
    total_water = sum(sum(row) for row in grid)
    
    # If there's no water or capacity is greater than or equal to total water, 
    # we only need to lower the bucket once per well with water (if capacity > 0)
    if total_water == 0 or capacity >= total_water:
        return sum(1 for row in grid if any(row)) if capacity > 0 else 0
    
    # Calculate the number of times buckets need to be lowered
    # This is done by dividing the total water by the bucket capacity and rounding up
    # We use math.ceil for this purpose
    return math.ceil(total_water / capacity)