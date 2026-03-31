def by_length(arr):
    # Define a list of digit names corresponding to integers from 1 to 9
    nums = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    
    # Filter out numbers not in the range [1, 9] and sort them
    sorted_arr = sorted([num for num in arr if 1 <= num <= 9])
    
    # Reverse the array
    reversed_sorted_arr = sorted_arr[::-1]
    
    # Replace each number by its corresponding name from "One" to "Nine"
    result = [nums[i] for i in reversed_sorted_arr]
    
    return result