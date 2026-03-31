def by_length(arr):
    """
    Given an array of integers, sort the integers, reverse the resulting array,
    and replace each digit that is between 1 and 9 inclusive with its English
    name ("One" .. "Nine"). Any numbers outside 1–9 are ignored in the final
    result.

    Examples
    --------
    >>> by_length([2, 1, 1, 4, 5, 8, 2, 3])
    ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    >>> by_length([])
    []
    >>> by_length([1, -1, 55])
    ['One']
    """
    names = ["", "One", "Two", "Three", "Four", "Five",
             "Six", "Seven", "Eight", "Nine"]

    # Sort the entire array, then reverse it.
    sorted_reversed = sorted(arr, reverse=True)

    # Convert valid digits to names, ignoring others.
    return [names[num] for num in sorted_reversed if 1 <= num <= 9]