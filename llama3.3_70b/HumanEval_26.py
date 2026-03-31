from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    seen_more_than_once = set()

    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
        else:
            seen_more_than_once.add(num)

    return [num for num in result if num not in seen_more_than_once]