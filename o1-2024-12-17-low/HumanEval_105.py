def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> [1, 1, 2, 2, 3, 4, 5, 8]
            -> [8, 5, 4, 3, 2, 2, 1, 1]
      returns ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      returns []
    
      If the array has any number not in 1..9, ignore that number:
      arr = [1, -1, 55]
            -> sort valid numbers -> [1]
            -> reverse -> [1]
      returns ['One']
    """
    names = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }
    
    valid_numbers = [num for num in arr if 1 <= num <= 9]
    valid_numbers.sort()
    valid_numbers.reverse()
    
    return [names[num] for num in valid_numbers]