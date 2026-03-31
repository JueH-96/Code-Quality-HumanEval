from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 
    'nine'. Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 
    'six', 'seven', 'eight' and 'nine'. Return the string with numbers sorted from 
    smallest to largest """
    
    # Map words to their corresponding integer values.
    word_to_num = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, \
                   'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    # Map integer values back to their corresponding words.
    num_to_word = {v: k for k, v in word_to_num.items()}
    
    numbers_split = numbers.split(' ')  # Split the input string into a list of words.
    
    numbers_sorted = sorted([word_to_num[n] for n in numbers_split])  # Sort the integer values.
    
    return ' '.join(num_to_word[i] for i in numbers_sorted)  # Convert back to words and join into a string.