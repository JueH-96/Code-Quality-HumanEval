def by_length(arr):
    word_dict = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }
    filtered = [x for x in arr if 1 <= x <= 9]
    if not filtered:
        return []
    sorted_filtered = sorted(filtered)
    reversed_list = sorted_filtered[::-1]  # Reverse the list
    result = [word_dict[x] for x in reversed_list]
    return result