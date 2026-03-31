def generate_integers(a, b):
    lower = min(a, b)
    upper = max(a, b)
    result_set = set()
    
    for n in range(lower, upper + 1):
        for c in str(n):
            x = int(c)
            if x % 2 == 0 and lower <= x <= upper:
                result_set.add(x)
                
    return sorted(result_set)