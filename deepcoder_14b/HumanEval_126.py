def is_ascending_and_unique(lst):
    # Check if the list is non-decreasing
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    # Check for duplicates by comparing lengths of set and original list
    if len(set(lst)) != len(lst):
        return False
    # If all conditions are satisfied
    return True

# Example usage:
print(is_ascending_and_unique([1, 2, 3, 4]))  # Output: True
print(is_ascending_and_unique([1, 2, 2, 3]))  # Output: False
print(is_ascending_and_unique([5]))            # Output: True