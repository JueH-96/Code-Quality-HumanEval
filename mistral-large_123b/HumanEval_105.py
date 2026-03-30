def by_length(arr):
    digit_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    valid_numbers = [x for x in arr if 1 <= x <= 9]
    sorted_valid_numbers = sorted(valid_numbers)
    reversed_sorted_valid_numbers = list(reversed(sorted_valid_numbers))
    result = [digit_names[x - 1] for x in reversed_sorted_valid_numbers]
    return result