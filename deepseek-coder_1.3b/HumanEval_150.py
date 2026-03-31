def x_or_y(n, x, y):  # Defining the function with parameters n (input),x & y as output.  
    def isPrimeNumberChecker(nums):     # This inner method checks whether a number in an iterable list of numbers num or not if it's prime then return True else False .     
        for i in range(2, int(n ** 0.5) + 1):          # We only need to check divisibility up till square root as any factor will have already been checked below that point using 'range'.        
            if n % i == 0:                   # If the number is evenly divided then it's not a prime and we return False.  It won’t reach this condition otherwise (as loop checks only for factors till sqrt(n)).         
                return False                           # Returning false as per requirement of function 'isPrimeNumberChecker'.     
        else:                             # If none found then it's a prime and we will be returning True.  It won’t reach this condition otherwise (as loop checks all numbers).      
            return True                    # We are using the term "prime" in terms of checking primality so, 'return true'.     
     if isPrimeNumberChecker(n):         # Checking whether n or not. If it's a prime then proceed to print y else x as per requirement for function call .   
        return 1                         # Return value will be changed according the condition inside this block (in our case, we want 'x').    
                
# Test cases:                    
print(f"{n} {isPrimeNumberChecker([i])}")              # Prints whether n is a prime or not and also prints x if it's Prime else y.   It will print the output as per requirement inside brackets ().  For example, for 'x_or_y(7 ,34,12)' expected outputs would be:
#print('Is ',n,'prime?', isPrimeNumberChecker([i]))      # Prints whether n or not and also prints x if it's prime else y.  It will print the output as per requirement inside brackets (). For example, 'is Prime Number Checker(7)' expected outputs would be:
#print('Is ',n,'prime?', isPrimeNumberChecker([i]))   # Print what you’re testing and also prints x if it's prime else y.  It will print the output as per requirement inside brackets (). For example, 'is Prime Number Checker(7)' expected outputs would be: