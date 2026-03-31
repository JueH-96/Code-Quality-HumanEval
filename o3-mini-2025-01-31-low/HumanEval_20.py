def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort numbers
    sorted_numbers = sorted(numbers)
    # Initialize the minimum difference as infinity and establish a pair placeholder.
    min_diff = float('inf')
    closest_pair = (None, None)
    
    # Iterate through sorted list to find minimal adjacent difference
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    
    return closest_pair