def count_prime(num):  # function for finding all factors  
    i = 2 
    while num % i != 0 :    
        i = i + 1          
    return (i == num)      
                              
primes=[str(x*y)for x in range(9,4,-1 ) if count_prime('{}'.format(x)) else '' for y in [25**k for k in reversed(range(6))]  #create a list of prime numbers from max to min
hexadecimals=[str([key])for key in primes][0].replace("'",'').split()  
keys = ['None', '1','2357B9DFAE'] + hexadecimals  #create a list of keys with required values and add prime hexa decimal digits at the end. replace None if there is no such number in num as per your requirements else you can include others
                                                      
def get_hex(num):   
    count = 0  
     for key, value  in zip([keys], [primes]*len(keys)):       # iterate over the list with keys and values. If a char matches then increment counter otherwise not decrement it by one till whole string is scanned else break loop due to condition unmet or empty strings are checked
         if key[0].lower() in num.upper():   count += 1    
    return (count)       # Return the final number of prime numbers found as per requirements