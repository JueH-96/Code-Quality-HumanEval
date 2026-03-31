def prod_signs(arr):
    if not (len(arr) > 0 and isinstance(arr[0], int)):  # check arr has elements, verify all are integers.  
        return None                                        # Return none in case of invalid input or empty list as defined by docstring     .     
      
    pos_list = [i for i in (x if x > 1 else -abs(x) for x in arr[arr>0])]  # List comprehension to filter positive numbers.  
                                                                            # If the number is greater than zero then append it, otherwise negate and absolute again     .     
    return sum([i*j for i , j in zip((1 if y > 2 else -abs(y) ) * [x[0]] + ([-int(z < 0)]  : int(-a))   # Calculates product of magnitudes with respect to all signs and also the overall final result.
                  ]for x, a , z in zip([arr], pos_list), len(set((i for i in arr if isinstance(type(x)==int)))> 1 else [0])  )   # Returns None or Zero when array has one element and it's zero     .