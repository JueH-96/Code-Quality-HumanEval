from typing import List
DIGITS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def sort_numbers(numbers: str) -> str:
    numbers = numbers.split()
    sorted_numbers = sorted(numbers, key=lambda x: DIGITS.index(x))
    return ' '.join(sorted_numbers)