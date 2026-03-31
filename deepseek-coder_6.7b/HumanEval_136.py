def largest_smallest_integers(lst):
    max_neg = min_pos = float('-inf') if lst else None
    for i in lst:
        if i < 0 and i > max_neg: 
            max_neg = i
        elif i > 0 and (min_pos == float('-inf') or i < min_pos):  
            min_pos = i
    return (max_neg, None if min_pos == float('-inf') else min_pos)