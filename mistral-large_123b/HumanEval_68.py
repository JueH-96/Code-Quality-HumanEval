def pluck(arr):
    min_even = float('inf')
    min_index = -1

    for i, value in enumerate(arr):
        if value % 2 == 0 and value < min_even:
            min_even = value
            min_index = i

    if min_index == -1:
        return []
    else:
        return [min_even, min_index]