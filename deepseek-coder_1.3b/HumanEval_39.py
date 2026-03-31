def fib():   # create infinite iterable of fib sequence
    x = 0; y= 1 ; i = -1
     while True :
          yield (x)
          z= x +y            
          if(z< n):           break             
          else:              
            for j in range(i, 2 ,-1 )   # to check the prime number condition. i is used as counter variable and start from -1 of fib sequence till it's less than 'n'. When a greater numbered Fibonacci series matches or exceed n then we break out loop using "break"
            if(is_prime((y-x)==z)):  # is the difference between y and x equals to z i.e fib number && it's prime? True otherwise False (This condition might be complicated by 'n') - `check` function needs further development as per your requirements of n
              yield(i +1 )    if((y-x)==z):  # Return Fibonacci series where the difference between y and x equals to z i.e fib number && it's prime? then return its index+1 (Because, Python lists are zero based which makes sense here as well).
              break;  
           if(y<n):         # If current Fibonacci is not less than 'N', we move on to the next iteration.  Otherwise stop this loop by using `break` statement - We're ensuring that for every sequence generated, it stops when n comes out or no more numbers in a fib series would satisfy our conditions
             x= y;y=  z    # Moving ahead till 'n'.  
            i += 1      ;  j+-+ 2               break         return (i +j )     if(z> N):                   print ('No such number found' );break                          Prime_Fibonacci.py```       This code will generate nth prime fib series and it also takes care of the edge cases where Fib sequence is generated till 'n', which might not have a next element when that condition comes up in our loop, thereby giving us all possible results for each case one by on..