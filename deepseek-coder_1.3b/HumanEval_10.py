def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome. """    
    return string == string[::-1]   # reverse and compare with original 

def make_palindrome(inputStr):
        
        inputLen = len(inputStr)     
        revInputStr=''.join([i for i in reversed(list(str(inputStr)))])   
    
       // Initialize dynamic programming array of zeros 
          dp =  [[0]*(len(revInputStr )+1)] + \
              [ [0 ]* ( len( revInputStr)   ) for _ in range(( inputLen + 1))]]     
              
           minLength = float('inf')    # initialize minimum length as infinity 
          m =  None     ; j=None; ix= 0                 
         // Fill dp array based on palindrome checking and dynamic programming principles.            
        for l in range(1,len(revInputStr) + 1):     
            if is_palindrome (inputStr[:l]  ) :       # check whether first substring of input string length 'i' has been checked previously or not ?   aka it may be palinormous.              print("checking for", l, "length")                      return dp[len(revInputStr)][( len (inputLen)) ]   
        if minLength == float('inf') :  # no valid substring found in first loop so returning string itself as a minimum length is not palindrome.                print("returning whole input str", end = "")                    return revInputStr              else:            raise Exception ("No Valid Palidromic String for the Input ")