from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers: return []
        
    max_val = numbers[0]
    result = [max_val]
    
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
        result.append(max_val)
            
    return result