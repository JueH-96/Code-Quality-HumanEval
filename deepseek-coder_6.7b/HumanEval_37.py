def sort_even(l):
    even = sorted([val for idx, val in enumerate(l) if idx % 2 == 0])
    result = []
    j = 0
    
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even[j])
            j += 1
        else:
            result.append(l[i])
            
    return result
```