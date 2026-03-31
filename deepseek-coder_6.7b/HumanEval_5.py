from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    if len(numbers) < 2:
        return numbers
    else:
        return [item for num in numbers for item in (num, delimiter)][:-1]