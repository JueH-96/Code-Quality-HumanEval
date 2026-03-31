def by_length(arr):
    valid = [x for x in arr if 1 <= x <= 9]
    sorted_valid = sorted(valid)
    reversed_sorted = sorted_valid[::-1]
    mapping = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    return [mapping[x] for x in reversed_sorted]