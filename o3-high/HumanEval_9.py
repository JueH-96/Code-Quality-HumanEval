from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list containing the running
    (rolling) maximum up to each position.

    Examples
    --------
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([])
    []
    >>> rolling_max([5, 4, 3])
    [5, 5, 5]
    """
    rolling = []
    current_max = None
    for num in numbers:
        if current_max is None or num > current_max:
            current_max = num
        rolling.append(current_max)
    return rolling