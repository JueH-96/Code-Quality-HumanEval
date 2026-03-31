from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers.")
    sorted_nums = sorted(numbers)
    best_diff = float('inf')
    best_pair = (sorted_nums[0], sorted_nums[1])
    for prev, curr in zip(sorted_nums, sorted_nums[1:]):
        diff = curr - prev
        if diff < best_diff:
            best_diff = diff
            best_pair = (prev, curr)
            if best_diff == 0:
                break
    return best_pair