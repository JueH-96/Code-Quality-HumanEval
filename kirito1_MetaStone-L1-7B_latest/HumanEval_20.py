def find_min_difference_pair(numbers):
    sorted_numbers = sorted(numbers)
    min_diff = float('inf')
    best_pair = None
    
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i+1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
            best_pair = (sorted_numbers[i], sorted_numbers[i+1])
    
    return best_pair