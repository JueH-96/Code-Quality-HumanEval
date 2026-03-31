def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t. If there is any number greater or equal to 't' then return False otherwise it returns true."""    
   # iterate through each item of given input and check conditions 
    for num_item in l :        
        if (num_item >= t):            
            return False          
         
    else:             
       return True