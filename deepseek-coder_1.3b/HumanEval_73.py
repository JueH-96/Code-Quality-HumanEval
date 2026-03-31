def smallest_change(arr):  
    changes = 0     # variable storing the number of times array needs changed in order for it palindromic     
                    # initialize counter as zero (changes) when we start iterating from both ends simultaneously      
        
        left, right= 0 , len(arr)-1  # Initialize two pointers starting positions at each end    
          
    while left <=right:              # Iterate until the elements are not equal on either side of array  
            if arr[left] != arr[right]:      # If element is different, increment counter by one.        
                changes+= 1                      # This will take a change for every pair that has difference         
                                                  # when we move towards the center from both ends until they match    
                                                                             
            left += 1                          # Increment 'left' pointer if it was not equal to its right counterpart. 
                while arr[right] != arr[left]:   # If current element in array is different, increment and decrements "right"         
                    changes -= 1                       # Pointer towards the center will be moved one step forward until they match        
            if(changes == 0):                  # In case all elements are same so we return zero     
                break    
        right-=  1                             # Decrease 'right' pointer as soon it matches with its left counterpart. 
    return changes //2                         # Return total number of change which is half because each element in array must be changed to make palindromic      
```     
You can test this function using:    `print(smallest_change([1,43])) => 0 print(smallest_change(['a','b', 'c'])) =>  2 `. This works best for even length arrays and when the array has a balance of elements at both ends (either odd or even).