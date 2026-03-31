def sort_even(l: list):
    even_index_elements = [x for i, x in enumerate(l) if i % 2 == 0]
    even_index_elements.sort()
    
    result = l[:]
    for i, element in enumerate(result):
        if i % 2 == 0:
            result[i] = even_index_elements.pop(0)
            
    return result