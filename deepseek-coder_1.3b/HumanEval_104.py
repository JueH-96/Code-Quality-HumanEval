def unique_digits(x):
    # create an empty set to hold the final output values as they can only be in one element by definition 
    result = []  
    
    for num in x :           
        digits=str(num)        
		# convert list of numbers into a string, split it up and check each digit if its an even number or not. If all are odd then append to the final output set (as we only want unique elements). 
		 # sorted function is used for sorting in ascending order by default which will be [1523].sort() ==>[1, 2 ,3] if you call .sorted([int(i)for i in str_num]) it return a list of digits but now we want to keep the output as sorted integers not string.
        result += sorted({digit for digit in ''.join(str(x))})   # converting int into strings and then concatenating them  (because join is used on iterable) .then looping through each character within that joined str, adding it to a set since we don't care about duplicate entries.
    return [int(''.join([i for i in sorted(str_num)]))] if result else [] # converting the final output list into strings and then joining them back together because join is used on iterable which makes us string, so after that it converts all of those characters to integers again.