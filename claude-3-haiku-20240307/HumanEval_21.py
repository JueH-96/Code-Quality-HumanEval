def rescale_to_unit(numbers: List[float]) -> List[float]:
    a = min(numbers)
    b = max(numbers)
    return [(x - a) / (b - a) for x in numbers]