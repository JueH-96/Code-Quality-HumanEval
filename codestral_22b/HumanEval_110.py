def exchange(lst1, lst2):
    # Separate even and odd numbers in both lists
    even_lst1 = [x for x in lst1 if x % 2 == 0]
    odd_lst1 = [x for x in lst1 if x % 2 != 0]
    even_lst2 = [x for x in lst2 if x % 2 == 0]

    # If the number of odd elements in lst1 is greater than the number of even elements in lst2, return "NO"
    if len(odd_lst1) > len(even_lst2):
        return "NO"
    else:
        return "YES"