def max_fill(grid, bucket_capacity):
       import math
       total = sum([sum(row) for row in grid])
       return math.ceil(total / bucket_capacity)