def search(lst):
    lst.sort(reverse=True)  # sort list in descending order
    for i, num in enumerate(lst):
        if i >= num and (i == 0 or i != lst[i-1]):  # check frequency of number is greater than or equal to itself
            return i
    return -1