def sort_third(l: list):
    sorted_third = sorted([x for i, x in enumerate(l) if (i+1) % 3 == 0])
    result = []
    
    for i, x in enumerate(l):
        if (i+1) % 3 == 0:
            result.append(sorted_third.pop(0))
        else:
            result.append(x)
            
    return result