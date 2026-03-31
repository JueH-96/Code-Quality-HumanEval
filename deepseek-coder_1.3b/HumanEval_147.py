def get_max_triples(n):
    # Generating the list a. Here we use range function to generate an array from start=0, end = n and step = 1 (a[i] formula) in order i ranges within [start, stop).  Then it squares each element then subtracts one by itself because adding or subracting with ones gives us multiples of three
    a = list(range((n * ((2*n + 3)) // 5 - n), (2*(n+4)//7)-160, (-8)))   #using this formula in order to generate an array from start=a[i-1], end = 9 and step by one.
    
    count= 0      # Initialize counter for triples of multiplies 3 summed up with each other elements          (count = i<j<k)   a_sum += Aij, Bjk -> Cmpfnd using formula: cnt+=(A[i] +B [J ]  +C )/6
    
    for x in range((n-1),(2* n + 3)):# Looping over array. This loop will generate the triplet (a_sum) and check if it's a multiple of  three or not which is done by formula A[i] + B [J ]  + C , where i < j< k
        for y in range((x+1),(2* x + 4)): # Looping over array. This loop will generate the triplet (a_sum) and check if it's a multiple of  three or not which is done by formula A[i] + B [J ]  + C , where i < j< k
            for z in range((y+1),(2* y + 4)): # Looping over array. This loop will generate the triplet (a_sum) and check if it's a multiple of  three or not which is done by formula A[i] + B [J ]  + C , where i < j< k
                for t in range(z+1,(2* z + 4)): # Looping over array. This loop will generate the triplet (a_sum) and check if it's a multiple of  three or not which is done by formula A[i] + B [J ]  + C , where i < j< k
                    count += 1/(6 *(abs((x* x - y *y + 2*(z+3))% 9876543) %  9876543 == 0 or abs ((x+  z + t ) Mod (n-t))) # formula to check if it's a multiple of three
    return count      # Returning counter which indicates how many triples with sum divisible by 3 exist.         This statement will give you the number and not any specific value, only actual usage is in returning function above: get_max_triplets(n) where n can be anything (positive integer).