from typing import List
import itertools
    
def has_close_elements(numbers: List[float], threshold: float) -> bool :
    """ Check if in given list of numbers, are any two numbers closer to each other than 
        Given Threshold. If yes then return True else False at end"""  
      
         # Using itertools combinations method for all possible pairs from index till last element (excluded) with step as one pair is a set operation in python which can be used instead of list comprehension or map function to check if any two numbers are closer than threshold. 
    return bool(next((itertools.combinations(numbers,2)), False))   ## Return True for found and false when no match was discovered by iterator else the next method returns None (default value) which is converted into a boolean `False` in Python language so that we can use it directly as an if condition resultant of this function.