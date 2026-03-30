def sort_even(l: list):
    even_indices = sorted(l[::2])
    l[::2] = even_indices
    return l