def sort_third(l: list):
    new_l = []
    j = 0
    indices_to_sort = [i for i in range(len(l)) if i % 3 == 0]
    sorted_vals = sorted([l[i] for i in indices_to_sort])
    
    for i in range(len(l)):
        if i % 3 == 0:
            new_l.append(sorted_vals[j])
            j += 1
        else:
            new_l.append(l[i])
    
    return new_l