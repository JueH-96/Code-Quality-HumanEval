import re   # Python's built-in import statement to use regular expressions. 
            
def fruit_distribution(s, n):    
    numbers = list(map(int, re.findall('\d+', s)))      # List comprehension and map function from python stdlib - find all digits in string (numbers) then convert them to int type using built-in Python functions  're' for regular expressions'.  
    numbers = sorted([n[1], n[-2]])                     # Sorting the list so that biggest number is at last. This handles situations when there are more than one mango (max and second max) in total fruit distribution    
                                                       
                                                                           
        return abs(numbers[0]- numbers[1]) +n    # returning difference between two largest values plus original n which represents all fruits distributed so far, if both of them were positive then it means there was no mango. In that case we add the remaining value in total basket '+' sign (abs)