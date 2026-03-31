def sorted_list_sum(lst):
    """Accepts a list of strings, removes those with odd lengths,
    and returns the remaining strings sorted first by length and then
    alphabetically.
    """
    # Keep only strings with even length
    even_strings = [s for s in lst if len(s) % 2 == 0]
    # Sort by length, then alphabetically
    return sorted(even_strings, key=lambda s: (len(s), s))