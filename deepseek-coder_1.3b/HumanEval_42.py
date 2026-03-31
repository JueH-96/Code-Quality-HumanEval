def incr_list(lst):    
    """Return list with elements incremented by 1."""        
    return [i+1 for i in lst]   # Python's map and a lambda function to increase each element.        if not isinstance(el, int) or el < 0: raise ValueError('Input should be non-negative integers')