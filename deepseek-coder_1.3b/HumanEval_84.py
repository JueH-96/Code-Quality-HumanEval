def solve(N):
    if N < 0 : # checking whether input is not a positive number. If so, return an error message to user or handle the edge case in your program accordingly such as returning None / Exception etc..
        print("Input must be non-negative integer.") 
    
   else:        
       def add_binary(n): # defining recursive function which will convert decimal number into binary. Call this inside our main solve() to use it properly in the required context of n being passed as an argument for solving problem's requirements or constraints defined by task description (e.g., 10^4 < N < 2*10 ^3)
           if(n == 0): # base condition, when number becomes zero stop recursion and return string representation till then in reverse order that is to get reversed binary value of the input decimal integer n as we are converting from decimals into binaries. 
               return ''    
            else:        
                return add_binary(n //2) + str(n % 2) # recursive call, by dividing number with two and appending remainder to end of the string obtained till now in each step until n becomes zero which indicates we have reached base condition. Now convert reversed binary result into decimal using Python's built-in int() function (second parameter set as 'binary'), then return it for usage according requirements or constraints defined by task description, e.g., summed up all the bits in our processed number
       res = add_binary(N) # calling recursive method with input N to get its binary form and convert into a string format first which we can reverse as per problem's requirement (e.g.: 147 => 0b1100), then turn this reversed version back in decimal via int() function, return it for usage according requirements or constraints defined by task description
       if N<=5 : # checking whether input is a small number and print out the result to user as per problem's requirement.  If so handle edge cases such case (easy solution can be handled here) in your program accordingly like returning None / Exception etc..        
           return res