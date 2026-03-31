def sort_third(lst):
    # Create a copy of the original list to avoid modifying it directly
    new_list = list(lst)
    
    # Determine the indices where elements should be sorted (every 3rd element starting from index 0)
    indices = [i for i in range(len(new_list)) if i % 3 == 0]
    
    # Extract the elements at these indices from the original list
    elements_to_sort = [lst[i] for i in indices]
    
    # Sort the extracted elements
    sorted_elements = sorted(elements_to_sort)
    
    # Assign the sorted elements back to their respective positions in the new list
    for idx, value in zip(indices, sorted_elements):
        new_list[idx] = value
    
    return new_list