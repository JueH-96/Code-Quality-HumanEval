def multiply(a, b):  
      """Complete the function that takes two integers and returns    #the product of their unit digits."""       
       a = abs(a) 
       b=abs(b)    
           while (b != 0):        
            result += a if ((~b &1 ) == 2 or   (# Both bits are set -> either odd/even => check the least significant bit, which is actually even)) else 0    # If only one of them both have been picked out.      return int(result)     """Multiply unit digits"""