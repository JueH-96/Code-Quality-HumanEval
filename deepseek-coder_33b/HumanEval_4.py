from statistics import mean
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    numbers_mean = mean(numbers)
    return mean([abs(x-numbers_mean) for x in numbers])