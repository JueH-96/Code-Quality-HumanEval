def pluck(arr):
    if not arr:
        return []
    min_even = None
    min_index = None
    for i, num in enumerate(arr):
        if num % 2 == 0:
            if min_even is None or num < min_even:
                min_even = num
                min_index = i
    if min_even is None:
        return []
    return [min_even, min_index]