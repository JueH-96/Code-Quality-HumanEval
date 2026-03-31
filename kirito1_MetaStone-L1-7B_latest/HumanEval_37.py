def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    evens = l[::2]           # Extract elements at even indices
    sorted_evens = sorted(evens)  # Sort the extracted elements
    
    result = []
    e_ptr = 0                # Pointer to track the next element in sorted_evens
    
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(sorted_evens[e_ptr])
            e_ptr += 1
        else:
            result.append(l[i])
    
    return result