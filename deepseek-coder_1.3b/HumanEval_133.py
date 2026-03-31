import math   # Importing python's Math module for ceil function.
def sum_squares(lst):    
    return sum([math.ceil(i)**2 for i in lst])      // square each number and then add them up all at once inside a list comprehension, round the result using math ceiling to make sure we get an upper integer value first (to closest higher int). After that pass this whole new modified list into sum() function.
``` 
Test your code with different examples:  
print(sum_squares([1,2,3]))      # output should be : 14    - Explanation is in comments section above the solution if needed!     print (math.ceil()) // this will test how it works for positive numbers only as math ceiling function rounds up to nearest integer otherwise similar behavior can occur with negative and floating point values