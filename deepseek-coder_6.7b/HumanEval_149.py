def sorted_list_sum(lst):
    # Filter the strings with even lengths and sort them by length, then alphabetically.
    lst = [i for i in sorted([j for j in lst if len(j) % 2 == 0], key=lambda x: (len(x), x))]
    
    return lst
```
This function first filters out the strings that have odd lengths using a list comprehension. It does this by creating a new list containing only the elements of `lst` where the length of the element is an even number, achieved by looping over each element and checking its length with `len(j) % 2 == 0`. The resulting list is then sorted first by their lengths (using the key argument to achieve this), and then alphabetically using their string representation as the second sorting criterion. This is achieved through the lambda function `lambda x: (len(x), x)`, which returns a tuple containing the length of each element and that element itself. The sorted list is returned by the function.