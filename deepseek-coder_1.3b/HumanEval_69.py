def search(lst):
    freq = {}  # create a dictionary to store frequency of each number in lst.
    
    for i in range (len(lst)) :   # iterate over list and count frequency of numbers .
        if lst[i] not in freq:     
            freq [lst[i]] = 0      
        freq [lst[i]] += 1        
    
    for i in range (len(freq)) :   # iterate over dictionary. 
                             
        value = max_value  = list ( sorted((k, v)for k ,v in freq .items()))[-2][0]+max_value += lst[i]-1 if any ((x>y for x, y in zip(lst[:-1], [list ([val])*freq.get('{}'.format (w), w -  i   ], list([ val ] * freq . get (' {} '. format    + str    lst[i]))])))
        if max_value >= value: return min(max_value,lst[-1],key=lambda x:(x>0) and [sum((v-n for n in (sorted([k]) + list('%d' % i))if v > -2 else [] )for k ,i ].count()) or [-inf]
    return '-1';     # if no such pair exists then, we will get a negative number as output. In python 'neg_infinity'. So the function is returning it with neg infinity to handle all cases where there's not any valid result in given list else returns - 1;   Negative infinite integer value used for handling scenarios when no such pair exists ie, if none of your integers have frequency more than itself then return negative inf.