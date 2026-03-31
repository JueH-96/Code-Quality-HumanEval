def find_closest_pair(numbers):
    numbers_sorted = sorted(numbers)
    min_diff = float('inf')
    closest_a, closest_b = None, None
    
    for i in range(len(numbers_sorted) - 1):
        a = numbers_sorted[i]
        b = numbers_sorted[i + 1]
        current_diff = b - a
        
        if current_diff < min_diff:
            min_diff = current_diff
            closest_a, closest_b = a, b
    
    return (closest_a, closest_b)