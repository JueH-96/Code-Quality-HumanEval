def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions."""
    total = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            total += lst[i]
    return total