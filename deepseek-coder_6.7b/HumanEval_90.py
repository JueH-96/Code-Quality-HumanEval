def next_smallest(lst):
    if len(set(lst)) < 3:
        return None
    else:
        lst.sort()
        return lst[1]

print(next_smallest([1, 2, 3, 4, 5])) #== 2
print(next_smallest([5, 1, 4, 3, 2])) #== 2
print(next_smallest([])) #== None
print(next_smallest([1, 1])) #== None