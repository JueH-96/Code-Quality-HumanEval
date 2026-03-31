def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []
    result = [numbers[0]]
    for n in numbers[1:]:
        result.append(delimeter)
        result.append(n)
    return result