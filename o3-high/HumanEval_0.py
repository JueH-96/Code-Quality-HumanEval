from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check whether there are at least two numbers in the list whose absolute
    difference is smaller than the given threshold.

    Parameters
    ----------
    numbers : List[float]
        The list of floating-point numbers to examine.
    threshold : float
        The distance below which two distinct numbers are considered "close".

    Returns
    -------
    bool
        True if any pair of numbers is closer than `threshold`, False otherwise.

    Examples
    --------
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) < 2 or threshold <= 0:
        return False

    sorted_numbers = sorted(numbers)
    for a, b in zip(sorted_numbers, sorted_numbers[1:]):
        if b - a < threshold:
            return True
    return False