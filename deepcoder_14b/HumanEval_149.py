def sorted_list_sum(lst):
    # Filter out words with odd lengths
    filtered = [word for word in lst if len(word) % 2 == 0]
    # Sort by length and then alphabetically
    sorted_list = sorted(filtered, key=lambda x: (len(x), x))
    return sorted_list