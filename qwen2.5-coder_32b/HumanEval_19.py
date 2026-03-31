from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    num_to_word = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    word_to_num = {word: num for num, word in num_to_word.items()}
    
    # Split the input string into a list of words
    words = numbers.split()
    
    # Convert words to their corresponding numeric values
    nums = [word_to_num[word] for word in words]
    
    # Sort the numeric values
    nums.sort()
    
    # Convert sorted numeric values back to words
    sorted_words = [num_to_word[num] for num in nums]
    
    # Join the sorted words into a single string
    return ' '.join(sorted_words)