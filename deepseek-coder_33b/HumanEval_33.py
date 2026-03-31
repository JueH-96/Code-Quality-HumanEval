def sort_third(l: list):
    indices = [i for i in range(len(l)) if (i+1) % 3 == 0]
    third_values = sorted([l[i] for i in indices])
    
    result = l[:]
    for i, index in enumerate(indices):
        result[index] = third_values[i]
        
    return result