def next_smallest(lst):
    l = set(sorted([x for x in sorted(set(lst))])) # get unique numbers and sort them, then eliminate duplicates by converting list to a Set (which automatically removes any duplicate items) before it's converted back into List. 2nd step 'for...in', so you will iterate over each item once
    if len(l) >= 1:  
        return next(x for x in l[1:] if not sorted([x]) < list(set(next((y, index_) for y,index_ in enumerate(sorted([x])))) ) # continue after sorting by values and then getting its 2nd smallest number (if any)
    return None   # If the set doesn't have more than one distinct element.    
```         
This function first eliminates duplication from list, sorts it in ascending order while also preserving indices for easy access later on - by using enumerate() method to index each value of sorted array and then continue looping through rest elements until we find the second smallest number (2nd item after sort).  If there is no such element or if all numbers are same, None will be returned.