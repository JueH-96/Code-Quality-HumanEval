def circular_shift(x, shift):
    # Convert integer x into string and reverse order of digits in str format to allow rotations later on right side  
     orig = [char for char in str(abs(x))]         
      if (orig[0] == '-'  ) :                     
         return "-"+''.join(''.join([str(ord(i)-48)for i in '739']).lstrip("-")   #convert - sign to digit and then rotate right, for the rest of rotation reverse as above    """    >>> circular_shift(-120,-5), '-6'