def rescale_to_unit(numbers):
    min_val = min(numbers)
    max_val = max(numbers)
    
    if min_val == max_val:
        return [0.5] * len(numbers)  # All elements are the same, just return a list of all 0.5s

    return [(x - min_val) / (max_val - min_val) for x in numbers]