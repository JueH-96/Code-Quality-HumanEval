def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
    """
    num_to_name = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    
    # Filter numbers between 1 and 9
    filtered_numbers = [num for num in arr if 1 <= num <= 9]
    
    # Sort the filtered numbers
    sorted_numbers = sorted(filtered_numbers)
    
    # Reverse the sorted numbers
    reversed_numbers = sorted_numbers[::-1]
    
    # Replace each number with its corresponding name
    result = [num_to_name[num] for num in reversed_numbers]
    
    return result