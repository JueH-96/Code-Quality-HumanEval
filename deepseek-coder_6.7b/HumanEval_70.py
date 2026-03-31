def strange_sort_list(lst):
    # Create a sorted copy of the input list
    sort_lst = sorted(lst)
    
    result = []
    while sort_lst:
        # Take smallest element
        result.append(sort_lst.pop(0))
        if sort_lst: 
            # Then take largest element
            result.append(sort_lst.pop())
    
    return result