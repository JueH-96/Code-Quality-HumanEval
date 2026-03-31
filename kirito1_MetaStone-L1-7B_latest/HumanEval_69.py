def search(lst):
    # Create a frequency dictionary to count occurrences of each number
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Collect all numbers that meet the condition (frequency >= number)
    candidates = [num for num, cnt in counts.items() if cnt >= num]
    
    # Return the maximum candidate if any exist; otherwise return -1
    return max(candidates) if candidates else -1