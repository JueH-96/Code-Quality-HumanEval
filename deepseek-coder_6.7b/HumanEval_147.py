def get_max_triples(n):
    mod = [0]*3 # create an array of length 3 filled with zeros
    a = [0]*n   # create an integer array 'a' of length n filled with zeros
    
    for i in range(1, n+1):
        a[i-1] = (i**2 - i + 1)  # compute the value of each element using formula given
        mod[a[i-1] % 3] += 1   # increase count according to remainder of division by 3
    
    triple_count = 0  # initialize counter for triples to zero
    triple_count += (mod[0]*(mod[0]-1)*(mod[0]-2))//6  # add possible combinations for mod[0](remainder=0), i.e., multiples of 3
    triple_count += mod[1]*mod[2]*(mod[0])   # add possible combinations when remainder is 1 and 2 with remainder is 0
    
    return triple_count+(mod[1]*(mod[1]-1)*(mod[1]-2))//6 + (mod[2]*(mod[2]-1)*(mod[2]-2))//6   # add possible combinations for mod[1] and mod[2](remainders=1, 2), i.e., multiples of 3