def rounded_avg(n: int, m:int)->str or -1 :   # declare type hinting for parameters and return values 
    """You are given two positive integers n and m, and your task is to compute the average of the integers from n through m (including n and m). Round the answer to nearest integer. If input numbers aren't valid then returns -1"""     # Assuming docstring for this function in English 
    if not(isinstance(n, int) or isinstance(m ,int)) :   # ensure both parameters are integers only        
        raise ValueError("Both inputs must be of integer data type.")     
      
          
    elif n > m:     # If 'n' greater than `m` then return -1  since we have ensured that the function will not get here under normal circumstances. This is just to ensure code coverage   '''''           
        print("The input numbers don’t make logical sense.")     
        
    else :         
       avg = round((n + m)/2)     # compute average  from n and 'm' integers including both          
                              
                              """This part of the code computes binary representation"""              
        bin_val=bin(avg)[2:]   # convert computed integer to a string representing its numeric value in Binary. [0b1] is removed by slicing ‘[2: ]’              '''''                 
        
       return (f"{int(rounded_avg)}") if __name__ == "__main__":    # This line ensures the function won't be executed as a module, but can still run in an IDE.   It is used to call functions from other python files or standalone script for testing
     return bin_val  '''''        Here we use f-string formatting within string literal 'f"{int(rounded_avg)}"' and the backticks around variable names prevent them being recognized as Python code.   This function will not be executed if this line is commented out, hence it's a standalone testing file for functions like `bin` etc in python '''