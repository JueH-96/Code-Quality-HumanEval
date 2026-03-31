from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    range_of_values = max_number - min_number
    
    return [(i - min_number) / range_of_values for i in numbers]