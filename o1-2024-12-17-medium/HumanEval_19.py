def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    spelled = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    words = numbers.split()
    sorted_nums = sorted(words, key=lambda w: spelled.index(w))
    return " ".join(sorted_nums)