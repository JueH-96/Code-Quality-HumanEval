# Sample list of tuples
lst = [(2, 5), (1, 3), (1, 5), (2, 3)]

# Sorting the list based on row ascending and column descending
sorted_lst = sorted(lst, key=lambda x: (x[0], -x[1]))

# Print the sorted list
print(sorted_lst)