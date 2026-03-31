def next_smallest(lst):
    if len(set(lst)) < 2:   # if there are fewer than 2 unique elements in list, return None
        return None
    
    lst.sort()              # sort list
    
    smallest = lst[0]       # the smallest element is first after sorting
    
    for i in range(1, len(lst)):   # iterate over elements of sorted list
        if lst[i] > smallest:     # when we find an element greater than the smallest, it's the 2nd smallest
            return lst[i]          # so return this element and end function
            
    return None                 # if no such element was found, return None