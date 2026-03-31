from typing import List
import statistics


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean of the numbers
    mean_value = statistics.mean(numbers)
    
    # Calculate absolute deviations from the mean
    absolute_deviations = [abs(num - mean_value) for num in numbers]
    
    # Return the mean of these absolute deviations
    return statistics.mean(absolute_deviations)