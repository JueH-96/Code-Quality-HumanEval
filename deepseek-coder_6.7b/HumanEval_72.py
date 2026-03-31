def will_it_fly(q,w):
    # check for balanced 
    if q != q[::-1]: return False
    
    # calculate sum of weights
    total_weight = sum(q)

    # check weight condition
    if total_weight <= w: return True
      
    return False