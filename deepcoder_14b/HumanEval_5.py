from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []
    result = []
    prev = None
    for num in numbers:
        if prev is not None:
            result.append(delimeter)
        result.append(num)
        prev = num
    return result