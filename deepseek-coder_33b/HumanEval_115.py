def max_fill(grid, bucket_capacity):
    wells = [sum(row) for row in grid]
    wells.sort()
    num_buckets = 0
    
    while len(wells) > 0 and wells[-1] > 0:
        for i in range(len(wells)):
            if wells[i] == 0:
                break
            
            wells[i] -= bucket_capacity
        
        num_buckets += 1
    
    return num_buckets