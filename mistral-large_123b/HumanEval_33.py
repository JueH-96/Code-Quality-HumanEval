def sort_third(l: list):
    # Extract elements at indices divisible by three
    to_sort = [l[i] for i in range(len(l)) if i % 3 == 0]
    # Sort the extracted elements
    to_sort.sort()
    # Replace elements at indices divisible by three with sorted values
    result = l[:]
    sort_index = 0
    for i in range(len(l)):
        if i % 3 == 0:
            result[i] = to_sort[sort_index]
            sort_index += 1
    return result