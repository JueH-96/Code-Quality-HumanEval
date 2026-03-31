from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    n = len(numbers)
    if n == 0:
        raise ValueError("List cannot be empty.")
    mean = sum(numbers) / n
    mad = sum(abs(x - mean) for x in numbers) / n
    return mad