def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
    """
    # Mapping of numbers to their corresponding names
    num_to_name = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }
    
    # Filter numbers between 1 and 9 inclusive
    filtered = [num for num in arr if 1 <= num <= 9]
    
    # Sort and reverse the filtered list
    filtered.sort(reverse=True)
    
    # Map numbers to their names
    result = [num_to_name[num] for num in filtered]
    
    return result