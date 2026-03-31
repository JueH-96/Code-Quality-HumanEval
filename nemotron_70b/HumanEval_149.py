def sorted_list_sum(lst):
    """..."""  # docstring remains the same, but function name doesn't match specs; assuming typo and proceeding with 'sorted_list_sum' as is.

    return sorted([s for s in lst if len(s) % 2 == 0], key=lambda x: (len(x), x))