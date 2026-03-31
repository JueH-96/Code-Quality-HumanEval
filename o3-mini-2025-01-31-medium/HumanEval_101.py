import re

def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Use regex to split the string on commas and any whitespace.
    # The pattern [,\s]+ matches one or more commas or whitespace characters.
    return re.split(r"[,\s]+", s.strip())