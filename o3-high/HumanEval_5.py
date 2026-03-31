from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert `delimeter` between every pair of consecutive elements in `numbers`.
    
    Examples
    --------
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) <= 1:
        # Return a shallow copy to avoid mutating the original list
        return numbers[:]

    # Build the new list with delimiter values in between
    result: List[int] = []
    for idx, num in enumerate(numbers):
        if idx:
            result.append(delimeter)
        result.append(num)
    return result