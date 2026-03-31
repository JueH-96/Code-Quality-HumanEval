from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    count_ordered = OrderedDict((num, numbers.count(num)) for num in numbers)
    return [num for num, count in count_ordered.items() if count == 1]