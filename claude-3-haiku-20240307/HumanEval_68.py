def pluck(arr):
    if not arr:
        return []
    
    even_values = [value for value in arr if value % 2 == 0]
    if not even_values:
        return []
    
    smallest_even = min(even_values)
    index = next(i for i, x in enumerate(arr) if x == smallest_even)
    
    return [smallest_even, index]