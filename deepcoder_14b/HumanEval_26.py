def remove_duplicates(numbers):
    # Count the frequency of each number in the input list
    from collections import defaultdict
    freq = defaultdict(int)
    for x in numbers:
        freq[x] += 1
    
    # Build the result list including only elements with a frequency of one
    result = []
    for x in numbers:
        if freq[x] == 1:
            result.append(x)
    
    return result