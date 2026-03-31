def monotonic(l):
    incr = True
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            incr = False
    
    decr = True
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            decr = False
    
    return incr or decr