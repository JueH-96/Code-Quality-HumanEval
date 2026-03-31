def next_smallest(lst):
    unique_elements = list(set(lst))
    unique_elements.sort()
    return unique_elements[1] if len(unique_elements) > 1 else None