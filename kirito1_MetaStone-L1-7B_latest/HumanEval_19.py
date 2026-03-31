from typing import List

def sort_numbers(numbers: str) -> str:
    word_to_num = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    words = numbers.split()
    nums = [word_to_num[word] for word in words]
    sorted_nums = sorted(nums)
    num_to_word = {v: k for k, v in word_to_num.items()}
    sorted_words = [num_to_word[n] for n in sorted_nums]
    return ' '.join(sorted_words)