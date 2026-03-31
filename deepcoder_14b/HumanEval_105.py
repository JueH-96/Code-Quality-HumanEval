def by_length(arr):
    number_names = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    filtered = [x for x in arr if 1 <= x <= 9]
    if not filtered:
        return []
    sorted_desc = sorted(filtered, reverse=True)
    result = [number_names[x] for x in sorted_desc]
    return result