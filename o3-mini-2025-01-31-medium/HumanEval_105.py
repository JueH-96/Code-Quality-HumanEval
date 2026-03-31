def by_length(arr):
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
    # Filter out numbers that are not between 1 and 9
    filtered = [num for num in arr if num in mapping]
    # Sort and reverse the filtered list
    filtered.sort()
    filtered.reverse()
    # Map each number to its corresponding name
    return [mapping[num] for num in filtered]