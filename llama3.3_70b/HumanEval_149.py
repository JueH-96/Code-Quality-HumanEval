def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    filtered_list = [s for s in lst if len(s) % 2 == 0]
    
    # Sort the list by length and then alphabetically
    sorted_list = sorted(filtered_list, key=lambda x: (len(x), x))
    
    return sorted_list