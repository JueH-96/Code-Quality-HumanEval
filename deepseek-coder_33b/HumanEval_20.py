from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()  # sorting the array
    min_diff = float('inf')
    num1, num2 = 0, 0
    
    for i in range(len(numbers)-1):
        diff = abs(numbers[i+1] - numbers[i])
        
        if diff < min_diff:
            min_diff = diff
            num1, num2 = numbers[i], numbers[i+1]
    
    return (min(num1, num2), max(num1, num2))  # returning in sorted order