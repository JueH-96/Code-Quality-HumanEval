from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    numbers = sorted(set([round(n, 2) for n in numbers]))
    
    for i in range(len(numbers)-1):
        if abs(numbers[i+1] - numbers[i]) < threshold:
            return True
            
    return False