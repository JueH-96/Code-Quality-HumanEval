def by_length(arr):
    # sorting and reversing the array
    arr = sorted([i for i in arr if 1 <= i <= 9])[::-1]  
    
    # mapping integers to their names
    nums2words = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    
    # replacing each integer with its name
    return [nums2words[i] for i in arr]