from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """From the supplied list of numbers (length >= 2), return the two values
    that are closest to each other as (smaller, larger).
    """
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required.")

    sorted_nums = sorted(numbers)
    best_pair = (sorted_nums[0], sorted_nums[1])
    min_diff = abs(sorted_nums[1] - sorted_nums[0])

    for idx in range(1, len(sorted_nums) - 1):
        a, b = sorted_nums[idx], sorted_nums[idx + 1]
        diff = b - a  # non-negative since the list is sorted
        if diff < min_diff:
            min_diff = diff
            best_pair = (a, b)
        elif diff == min_diff and (a, b) < best_pair:
            # Tie-break by choosing the lexicographically smaller pair
            best_pair = (a, b)

    return best_pair