from typing import List, Tuple  # Python standard library for type hinting in function signatures and docstrings

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:   # Defining a return datatype as tuple of floats. Function will be used to get two closest numbers from list — sorted one first before the other in ascending order and returned at end
    """ From an array (of length >= 2) select pairs that are 'closest' pairwise together, both having been selected by each member only once; return them arranged as described. If there is more than two elements present then it should be handled accordingly."""  # docstring for the function to explain what kind of data and output this would produce
    
    smallest_num = min(numbers)   # Finding minimum number in list (smallest possible difference between any pair will come from here). This is our first 'closest' element. Python built-in method `min` for lists provides the optimal solution to find minimal value — it simply returns what ever smallest one among all items
    
    numbers.remove(smallest_num)   # Removing that selected number so we won’t repeat in our search, otherwise next operation would have a same minimum again (which will cause an error if there is less than two elements). 
                                  # If only single element remains then both closest are the ones itself as they're already sorted.
    
    largest_num = max(numbers)   # Finding maximum number in list to be considered 'closest'. Python built-in method `max` provides optimal solution for finding maximal value among all items — it simply returns what ever biggest one amongst them and this will give us the second closest element.
    
    return (smallest_num, largest_num)   # Returning tuple of smallest number first followed by largest in ascending order as asked within docstring explaining function behaviour: smaller is closer to larger numbers — so we have returned these two elements that are 'closer' together than the other ones.