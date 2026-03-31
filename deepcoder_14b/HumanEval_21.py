from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val = min(numbers)
    max_val = max(numbers)
    denominator = max_val - min_val
    if denominator == 0:
        return [0.0 for _ in numbers]
    else:
        return [(x - min_val) / denominator for x in numbers]