def get_odd_collatz(n):
    """Returns a sorted list of odd numbers in Collatz sequence"""
    
    # If n = 1, we're at the end of the sequence. Return [1].
    if n == 1:
        return [1]
  
    # If n is even, the next number in the sequence is n/2.
    elif n % 2 == 0:
        collatz_list = get_odd_collatz(n // 2)
        
    # Otherwise, if n is odd, the next number is 3*n + 1.
    else:
        collatz_list = get_odd_collatz(3 * n + 1)
    
    # If n is odd, append it to the list.
    if n % 2 != 0:
        collatz_list.append(n)
        
    return sorted(collatz_list)