def is_sorted(lst):
    # Check for duplicates first
    if len(set(lst)) != len(lst):
        return False
    # Now check if it's non-decreasing
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True