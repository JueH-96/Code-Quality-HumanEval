def largest_smallest_integers(lst):
    negative = [i for i in lst if i < 0]
    positive = [i for i in lst if i > 0]
    
    a = max(negative) if negative else None
    b = min(positive) if positive else None
    
    return (a, b)