from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    if not numbers:
        return result
    result.append(numbers[0])
    for number in numbers[1:]:
        result.append(delimeter)
        result.append(number)
    return result